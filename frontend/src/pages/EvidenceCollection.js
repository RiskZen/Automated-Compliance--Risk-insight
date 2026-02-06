import React, { useContext } from 'react';
import { AppContext } from '@/App';
import { motion } from 'framer-motion';
import { FileCheck, Zap, Clock, CheckCircle2, FileText, Activity } from 'lucide-react';

const EvidenceCollection = () => {
  const { evidence, controls, loading } = useContext(AppContext);

  const automatedEvidence = evidence.filter(e => e.automated);
  const manualEvidence = evidence.filter(e => !e.automated);
  const automationRate = evidence.length > 0
    ? ((automatedEvidence.length / evidence.length) * 100).toFixed(0)
    : 0;

  const getControlName = (controlId) => {
    const control = controls.find(c => c.id === controlId);
    return control ? control.name : 'Unknown Control';
  };

  const evidenceTypes = [...new Set(evidence.map(e => e.evidence_type))];

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <Activity className="h-12 w-12 text-blue-500 animate-spin" />
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <div className="mb-8">
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-slate-900 mb-2">Evidence Collection</h1>
          <p className="text-lg text-slate-600">Automated evidence gathering for continuous compliance</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-6">
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.1 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6"
            data-testid="metric-total-evidence"
          >
            <div className="flex items-center justify-between mb-4">
              <div className="h-10 w-10 rounded-full bg-blue-50 flex items-center justify-center">
                <FileCheck className="h-5 w-5 text-blue-600" />
              </div>
            </div>
            <p className="text-sm text-slate-500 mb-1">Total Evidence</p>
            <p className="text-3xl font-bold text-slate-900">{evidence.length}</p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.2 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6"
            data-testid="metric-automated"
          >
            <div className="flex items-center justify-between mb-4">
              <div className="h-10 w-10 rounded-full bg-green-50 flex items-center justify-center">
                <Zap className="h-5 w-5 text-green-600" />
              </div>
            </div>
            <p className="text-sm text-slate-500 mb-1">Automated</p>
            <p className="text-3xl font-bold text-slate-900">{automatedEvidence.length}</p>
            <p className="text-xs text-green-600 mt-2">{automationRate}% automation rate</p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.3 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6"
            data-testid="metric-manual"
          >
            <div className="flex items-center justify-between mb-4">
              <div className="h-10 w-10 rounded-full bg-amber-50 flex items-center justify-center">
                <Clock className="h-5 w-5 text-amber-600" />
              </div>
            </div>
            <p className="text-sm text-slate-500 mb-1">Manual</p>
            <p className="text-3xl font-bold text-slate-900">{manualEvidence.length}</p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.4 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6"
            data-testid="metric-evidence-types"
          >
            <div className="flex items-center justify-between mb-4">
              <div className="h-10 w-10 rounded-full bg-purple-50 flex items-center justify-center">
                <FileText className="h-5 w-5 text-purple-600" />
              </div>
            </div>
            <p className="text-sm text-slate-500 mb-1">Evidence Types</p>
            <p className="text-3xl font-bold text-slate-900">{evidenceTypes.length}</p>
          </motion.div>
        </div>

        <div className="bg-gradient-to-br from-green-50 to-emerald-50 rounded-lg border border-green-200 p-6 mb-6">
          <div className="flex items-start gap-4">
            <div className="h-12 w-12 rounded-full bg-green-600 flex items-center justify-center flex-shrink-0">
              <Zap className="h-6 w-6 text-white" />
            </div>
            <div>
              <h3 className="text-xl font-bold text-slate-900 mb-2">Automated Evidence Collection</h3>
              <p className="text-slate-700 mb-3">
                Our platform continuously collects evidence across all controls, reducing manual audit preparation time by 85%. 
                Real-time evidence collection ensures audit-readiness at all times.
              </p>
              <div className="flex flex-wrap gap-2">
                {evidenceTypes.map(type => (
                  <span
                    key={type}
                    className="px-3 py-1 bg-white border border-green-200 rounded-full text-sm font-medium text-green-800"
                  >
                    {type}
                  </span>
                ))}
              </div>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
          <h3 className="text-xl font-semibold text-slate-900 mb-4">Evidence Repository</h3>
          <div className="space-y-3">
            {evidence.map((ev, idx) => (
              <div
                key={ev.id}
                className="border border-slate-200 rounded-lg p-4 hover:border-blue-300 hover:shadow-md transition-all duration-200"
                data-testid={`evidence-item-${idx}`}
              >
                <div className="flex items-start justify-between">
                  <div className="flex-1">
                    <div className="flex items-center gap-3 mb-2">
                      <div className={`h-10 w-10 rounded-full flex items-center justify-center ${
                        ev.automated ? 'bg-green-100' : 'bg-amber-100'
                      }`}>
                        {ev.automated ? (
                          <Zap className="h-5 w-5 text-green-600" />
                        ) : (
                          <Clock className="h-5 w-5 text-amber-600" />
                        )}
                      </div>
                      <div>
                        <h4 className="font-semibold text-slate-900">{ev.description}</h4>
                        <p className="text-sm text-slate-600">Control: {getControlName(ev.control_id)}</p>
                      </div>
                    </div>

                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-3">
                      <div>
                        <p className="text-xs text-slate-500">Evidence Type</p>
                        <p className="text-sm font-medium text-slate-900">{ev.evidence_type}</p>
                      </div>
                      <div>
                        <p className="text-xs text-slate-500">Collection Method</p>
                        <div className="flex items-center gap-1">
                          {ev.automated ? (
                            <>
                              <Zap className="h-3 w-3 text-green-600" />
                              <span className="text-sm font-medium text-green-600">Automated</span>
                            </>
                          ) : (
                            <>
                              <Clock className="h-3 w-3 text-amber-600" />
                              <span className="text-sm font-medium text-amber-600">Manual</span>
                            </>
                          )}
                        </div>
                      </div>
                      <div>
                        <p className="text-xs text-slate-500">Status</p>
                        <div className="flex items-center gap-1">
                          <CheckCircle2 className="h-3 w-3 text-green-600" />
                          <span className="text-sm font-medium text-green-600">{ev.status}</span>
                        </div>
                      </div>
                      <div>
                        <p className="text-xs text-slate-500">Collected At</p>
                        <p className="text-sm font-medium text-slate-900">
                          {new Date(ev.collected_at).toLocaleDateString()}
                        </p>
                      </div>
                    </div>

                    {ev.automated && (
                      <div className="mt-3 p-3 bg-green-50 border border-green-200 rounded-lg">
                        <p className="text-xs text-green-800">
                          <strong>Automation Benefit:</strong> This evidence is collected automatically in real-time, 
                          ensuring continuous compliance and reducing manual audit preparation by 90%.
                        </p>
                      </div>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>

          {evidence.length === 0 && (
            <div className="text-center py-12">
              <FileCheck className="h-16 w-16 text-slate-300 mx-auto mb-4" />
              <p className="text-slate-600">No evidence collected yet</p>
            </div>
          )}
        </div>

        <div className="mt-6 bg-blue-50 border border-blue-200 rounded-lg p-6">
          <h3 className="text-lg font-semibold text-slate-900 mb-2">Automation Opportunities</h3>
          <p className="text-slate-700 mb-4">
            AI-powered analysis identifies additional evidence collection opportunities that can be automated:
          </p>
          <ul className="space-y-2">
            <li className="flex items-start gap-2">
              <CheckCircle2 className="h-5 w-5 text-blue-600 mt-0.5 flex-shrink-0" />
              <span className="text-slate-700">Automate quarterly access review evidence via API integration</span>
            </li>
            <li className="flex items-start gap-2">
              <CheckCircle2 className="h-5 w-5 text-blue-600 mt-0.5 flex-shrink-0" />
              <span className="text-slate-700">Real-time vendor assessment score collection</span>
            </li>
            <li className="flex items-start gap-2">
              <CheckCircle2 className="h-5 w-5 text-blue-600 mt-0.5 flex-shrink-0" />
              <span className="text-slate-700">Automated PIA completion tracking via workflow system</span>
            </li>
          </ul>
        </div>
      </motion.div>
    </div>
  );
};

export default EvidenceCollection;
