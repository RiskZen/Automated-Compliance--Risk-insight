import React, { useContext, useState } from 'react';
import { AppContext } from '@/App';
import { motion } from 'framer-motion';
import axios from 'axios';
import { ClipboardCheck, Upload, CheckCircle2, XCircle, Loader2, FileText, Calendar, User } from 'lucide-react';
import { toast } from 'sonner';

const ControlTesting = () => {
  const { unifiedControls, controlTests, setControlTests, evidence, loading, API, refreshData } = useContext(AppContext);
  const [selectedControl, setSelectedControl] = useState(null);
  const [testForm, setTestForm] = useState({
    tester: '',
    status: 'In Progress',
    result: '',
    notes: '',
  });
  const [uploadingEvidence, setUploadingEvidence] = useState(false);
  const [evidenceFile, setEvidenceFile] = useState(null);
  const [evidenceDescription, setEvidenceDescription] = useState('');

  const startTest = (control) => {
    setSelectedControl(control);
    setTestForm({
      tester: '',
      status: 'In Progress',
      result: '',
      notes: '',
    });
  };

  const submitTest = async (e) => {
    e.preventDefault();
    try {
      const testData = {
        unified_control_id: selectedControl.id,
        tester: testForm.tester,
        status: testForm.status,
        result: testForm.result,
        evidence_ids: [],
        notes: testForm.notes,
      };

      await axios.post(`${API}/control-tests`, testData);
      toast.success(`Control test ${testForm.result === 'Pass' ? 'passed' : 'failed'}`);
      
      if (testForm.result === 'Fail') {
        toast.info('Issue automatically created for failed control');
      }
      
      setSelectedControl(null);
      refreshData();
    } catch (error) {
      console.error('Error submitting test:', error);
      toast.error('Failed to submit test');
    }
  };

  const uploadEvidence = async (e) => {
    e.preventDefault();
    if (!evidenceFile) {
      toast.error('Please select a file');
      return;
    }

    setUploadingEvidence(true);
    try {
      const formData = new FormData();
      formData.append('file', evidenceFile);
      formData.append('control_test_id', 'manual-upload');
      formData.append('unified_control_id', selectedControl.id);
      formData.append('description', evidenceDescription);

      await axios.post(`${API}/evidence/upload`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });

      toast.success('Evidence uploaded successfully');
      setEvidenceFile(null);
      setEvidenceDescription('');
      refreshData();
    } catch (error) {
      console.error('Error uploading evidence:', error);
      toast.error('Failed to upload evidence');
    } finally {
      setUploadingEvidence(false);
    }
  };

  const getControlTests = (controlId) => {
    return controlTests.filter(t => t.unified_control_id === controlId).sort((a, b) => 
      new Date(b.test_date) - new Date(a.test_date)
    );
  };

  const getTestStatusColor = (result) => {
    if (result === 'Pass') return 'bg-green-100 text-green-800';
    if (result === 'Fail') return 'bg-red-100 text-red-800';
    return 'bg-yellow-100 text-yellow-800';
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <Loader2 className="h-12 w-12 text-blue-500 animate-spin" />
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
        <div className="mb-8">
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-slate-900 mb-2">Control Testing</h1>
          <p className="text-lg text-slate-600">Test controls and collect evidence (automated or manual)</p>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-6">
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Total Tests</p>
            <p className="text-3xl font-bold text-slate-900">{controlTests.length}</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Passed</p>
            <p className="text-3xl font-bold text-green-600">{controlTests.filter(t => t.result === 'Pass').length}</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Failed</p>
            <p className="text-3xl font-bold text-red-600">{controlTests.filter(t => t.result === 'Fail').length}</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Evidence Files</p>
            <p className="text-3xl font-bold text-slate-900">{evidence.length}</p>
          </div>
        </div>

        {/* Controls List */}
        <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
          <h3 className="text-xl font-semibold text-slate-900 mb-4">Unified Controls - Testing</h3>
          
          <div className="space-y-4">
            {unifiedControls.map((control) => {
              const tests = getControlTests(control.id);
              const latestTest = tests[0];
              
              return (
                <div key={control.id} className="border border-slate-200 rounded-lg p-4 hover:border-blue-300 transition-all" data-testid={`control-test-${control.id}`}>
                  <div className="flex items-start justify-between mb-3">
                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2">
                        <div className="px-2 py-1 bg-blue-100 text-blue-800 rounded text-xs font-mono font-semibold">
                          {control.ccf_id}
                        </div>
                        <h4 className="font-semibold text-slate-900">{control.name}</h4>
                        {latestTest && (
                          <span className={`px-3 py-1 rounded-full text-xs font-semibold ${getTestStatusColor(latestTest.result)}`}>
                            Last Test: {latestTest.result}
                          </span>
                        )}
                      </div>
                      <p className="text-sm text-slate-600 mb-2">{control.description}</p>
                      
                      <div className="flex items-center gap-4 text-xs text-slate-500">
                        <span>Type: <strong>{control.control_type}</strong></span>
                        <span>Frequency: <strong>{control.frequency}</strong></span>
                        <span>Tests: <strong>{tests.length}</strong></span>
                      </div>
                    </div>

                    <button
                      onClick={() => startTest(control)}
                      className="flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition-colors"
                      data-testid={`start-test-${control.id}`}
                    >
                      <ClipboardCheck className="h-4 w-4" />
                      Start Test
                    </button>
                  </div>

                  {/* Test History */}
                  {tests.length > 0 && (
                    <div className="mt-3 pt-3 border-t border-slate-200">
                      <p className="text-xs font-semibold text-slate-700 mb-2">Test History:</p>
                      <div className="space-y-2">
                        {tests.slice(0, 3).map((test) => (
                          <div key={test.id} className="flex items-center gap-3 text-xs">
                            {test.result === 'Pass' ? (
                              <CheckCircle2 className="h-4 w-4 text-green-600" />
                            ) : (
                              <XCircle className="h-4 w-4 text-red-600" />
                            )}
                            <span className="text-slate-600">
                              {new Date(test.test_date).toLocaleDateString()} - {test.tester} - {test.result}
                            </span>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>

        {/* Test Modal */}
        {selectedControl && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
            <div className="bg-white rounded-lg max-w-2xl w-full max-h-[90vh] overflow-y-auto">
              <div className="p-6">
                <h3 className="text-2xl font-bold text-slate-900 mb-4">Test Control: {selectedControl.name}</h3>
                
                <form onSubmit={submitTest} className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-slate-700 mb-1">Tester Name *</label>
                    <input
                      type="text"
                      value={testForm.tester}
                      onChange={(e) => setTestForm({ ...testForm, tester: e.target.value })}
                      placeholder="John Doe"
                      required
                      className="w-full px-3 py-2 border border-slate-300 rounded-md focus:ring-2 focus:ring-blue-500"
                    />
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-slate-700 mb-1">Test Status *</label>
                    <select
                      value={testForm.status}
                      onChange={(e) => setTestForm({ ...testForm, status: e.target.value })}
                      className="w-full px-3 py-2 border border-slate-300 rounded-md focus:ring-2 focus:ring-blue-500"
                    >
                      <option>Not Started</option>
                      <option>In Progress</option>
                      <option>Completed</option>
                    </select>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-slate-700 mb-1">Test Result *</label>
                    <div className="flex gap-4">
                      <label className="flex items-center gap-2 cursor-pointer">
                        <input
                          type="radio"
                          name="result"
                          value="Pass"
                          checked={testForm.result === 'Pass'}
                          onChange={(e) => setTestForm({ ...testForm, result: e.target.value })}
                          className="w-4 h-4 text-green-600"
                          required
                        />
                        <span className="flex items-center gap-1 text-sm font-medium text-slate-700">
                          <CheckCircle2 className="h-4 w-4 text-green-600" />
                          Pass
                        </span>
                      </label>
                      <label className="flex items-center gap-2 cursor-pointer">
                        <input
                          type="radio"
                          name="result"
                          value="Fail"
                          checked={testForm.result === 'Fail'}
                          onChange={(e) => setTestForm({ ...testForm, result: e.target.value })}
                          className="w-4 h-4 text-red-600"
                          required
                        />
                        <span className="flex items-center gap-1 text-sm font-medium text-slate-700">
                          <XCircle className="h-4 w-4 text-red-600" />
                          Fail
                        </span>
                      </label>
                    </div>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-slate-700 mb-1">Notes</label>
                    <textarea
                      value={testForm.notes}
                      onChange={(e) => setTestForm({ ...testForm, notes: e.target.value })}
                      placeholder="Test findings, observations..."
                      rows={4}
                      className="w-full px-3 py-2 border border-slate-300 rounded-md focus:ring-2 focus:ring-blue-500"
                    />
                  </div>

                  {/* Evidence Upload */}
                  {!selectedControl.automation_possible && (
                    <div className="bg-amber-50 border border-amber-200 rounded-lg p-4">
                      <h4 className="text-sm font-semibold text-amber-900 mb-3 flex items-center gap-2">
                        <Upload className="h-4 w-4" />
                        Upload Evidence (Manual)
                      </h4>
                      <div className="space-y-3">
                        <div>
                          <label className="block text-xs font-medium text-slate-700 mb-1">Evidence File</label>
                          <input
                            type="file"
                            onChange={(e) => setEvidenceFile(e.target.files[0])}
                            className="w-full text-sm"
                          />
                        </div>
                        <div>
                          <label className="block text-xs font-medium text-slate-700 mb-1">Description</label>
                          <input
                            type="text"
                            value={evidenceDescription}
                            onChange={(e) => setEvidenceDescription(e.target.value)}
                            placeholder="Access review report Q1 2026"
                            className="w-full px-2 py-1 text-sm border border-slate-300 rounded-md"
                          />
                        </div>
                        <button
                          type="button"
                          onClick={uploadEvidence}
                          disabled={uploadingEvidence}
                          className="w-full px-3 py-2 bg-amber-600 hover:bg-amber-700 text-white text-sm font-medium rounded-md disabled:opacity-50"
                        >
                          {uploadingEvidence ? 'Uploading...' : 'Upload Evidence'}
                        </button>
                      </div>
                    </div>
                  )}

                  {selectedControl.automation_possible && (
                    <div className="bg-green-50 border border-green-200 rounded-lg p-4">
                      <p className="text-sm text-green-800">
                        <strong>Automated Evidence Collection:</strong> Evidence is collected automatically for this control.
                      </p>
                    </div>
                  )}

                  <div className="flex gap-3 pt-4">
                    <button
                      type="submit"
                      className="flex-1 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg"
                      data-testid="submit-test"
                    >
                      Submit Test
                    </button>
                    <button
                      type="button"
                      onClick={() => setSelectedControl(null)}
                      className="px-4 py-2 bg-slate-200 hover:bg-slate-300 text-slate-700 font-medium rounded-lg"
                    >
                      Cancel
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        )}
      </motion.div>
    </div>
  );
};

export default ControlTesting;
