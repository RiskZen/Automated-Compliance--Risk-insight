import React, { useContext, useState } from 'react';
import { AppContext } from '@/App';
import { motion } from 'framer-motion';
import axios from 'axios';
import { AlertTriangle, Plus, Loader2, Clock, CheckCircle2, AlertCircle, Shield } from 'lucide-react';
import { toast } from 'sonner';

const IssueManagement = () => {
  const { issues, setIssues, unifiedControls, loading, API, refreshData } = useContext(AppContext);
  const [showCreate, setShowCreate] = useState(false);
  const [selectedIssue, setSelectedIssue] = useState(null);
  const [newIssue, setNewIssue] = useState({
    title: '',
    description: '',
    unified_control_id: '',
    severity: 'Medium',
    assigned_to: '',
    due_date: '',
  });
  const [exceptionForm, setExceptionForm] = useState({
    reason: '',
    approved_by: '',
    expiry_date: '',
  });

  const createIssue = async (e) => {
    e.preventDefault();
    try {
      await axios.post(`${API}/issues`, {
        ...newIssue,
        status: 'Open',
        has_exception: false,
      });
      toast.success('Issue created');
      setShowCreate(false);
      setNewIssue({ title: '', description: '', unified_control_id: '', severity: 'Medium', assigned_to: '', due_date: '' });
      refreshData();
    } catch (error) {
      console.error('Error creating issue:', error);
      toast.error('Failed to create issue');
    }
  };

  const updateIssueStatus = async (issueId, newStatus) => {
    try {
      await axios.patch(`${API}/issues/${issueId}/status?status=${newStatus}`);
      setIssues(issues.map(i => i.id === issueId ? { ...i, status: newStatus } : i));
      toast.success(`Issue ${newStatus}`);
    } catch (error) {
      console.error('Error updating issue:', error);
      toast.error('Failed to update issue');
    }
  };

  const addException = async (issueId) => {
    try {
      await axios.patch(`${API}/issues/${issueId}/exception`, {
        exception_details: exceptionForm
      });
      toast.success('Exception added');
      setSelectedIssue(null);
      refreshData();
    } catch (error) {
      console.error('Error adding exception:', error);
      toast.error('Failed to add exception');
    }
  };

  const getSeverityColor = (severity) => {
    switch (severity) {
      case 'Critical': return 'bg-red-100 text-red-800 border-red-300';
      case 'High': return 'bg-orange-100 text-orange-800 border-orange-300';
      case 'Medium': return 'bg-yellow-100 text-yellow-800 border-yellow-300';
      case 'Low': return 'bg-blue-100 text-blue-800 border-blue-300';
      default: return 'bg-slate-100 text-slate-800 border-slate-300';
    }
  };

  const getStatusColor = (status) => {
    switch (status) {
      case 'Open': return 'bg-red-100 text-red-800';
      case 'In Progress': return 'bg-yellow-100 text-yellow-800';
      case 'Resolved': return 'bg-green-100 text-green-800';
      case 'Closed': return 'bg-slate-100 text-slate-800';
      default: return 'bg-slate-100 text-slate-800';
    }
  };

  const issuesByStatus = {
    Open: issues.filter(i => i.status === 'Open'),
    'In Progress': issues.filter(i => i.status === 'In Progress'),
    Resolved: issues.filter(i => i.status === 'Resolved'),
    Closed: issues.filter(i => i.status === 'Closed'),
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
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-slate-900 mb-2">Issue Management</h1>
          <p className="text-lg text-slate-600">Track compliance issues with lifecycle management & exceptions</p>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-5 gap-6 mb-6">
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Total Issues</p>
            <p className="text-3xl font-bold text-slate-900">{issues.length}</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Open</p>
            <p className="text-3xl font-bold text-red-600">{issuesByStatus.Open.length}</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">In Progress</p>
            <p className="text-3xl font-bold text-yellow-600">{issuesByStatus['In Progress'].length}</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Resolved</p>
            <p className="text-3xl font-bold text-green-600">{issuesByStatus.Resolved.length}</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">With Exceptions</p>
            <p className="text-3xl font-bold text-purple-600">{issues.filter(i => i.has_exception).length}</p>
          </div>
        </div>

        {/* Create Issue Button */}
        <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6 mb-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-xl font-semibold text-slate-900">Issues</h3>
            <button
              onClick={() => setShowCreate(!showCreate)}
              className="flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg"
              data-testid="create-issue-btn"
            >
              <Plus className="h-5 w-5" />
              Create Issue
            </button>
          </div>

          {showCreate && (
            <form onSubmit={createIssue} className="bg-slate-50 rounded-lg p-4 mb-4">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="md:col-span-2">
                  <label className="block text-sm font-medium text-slate-700 mb-1">Title *</label>
                  <input type="text" value={newIssue.title} onChange={(e) => setNewIssue({ ...newIssue, title: e.target.value })} placeholder="Control test failed..." required className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div className="md:col-span-2">
                  <label className="block text-sm font-medium text-slate-700 mb-1">Description *</label>
                  <textarea value={newIssue.description} onChange={(e) => setNewIssue({ ...newIssue, description: e.target.value })} placeholder="Detailed description..." required rows={3} className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Related Control *</label>
                  <select value={newIssue.unified_control_id} onChange={(e) => setNewIssue({ ...newIssue, unified_control_id: e.target.value })} required className="w-full px-3 py-2 border border-slate-300 rounded-md">
                    <option value="">Select control...</option>
                    {unifiedControls.map(c => (
                      <option key={c.id} value={c.id}>{c.ccf_id} - {c.name}</option>
                    ))}
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Severity *</label>
                  <select value={newIssue.severity} onChange={(e) => setNewIssue({ ...newIssue, severity: e.target.value })} className="w-full px-3 py-2 border border-slate-300 rounded-md">
                    <option>Low</option>
                    <option>Medium</option>
                    <option>High</option>
                    <option>Critical</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Assigned To *</label>
                  <input type="text" value={newIssue.assigned_to} onChange={(e) => setNewIssue({ ...newIssue, assigned_to: e.target.value })} placeholder="Team member" required className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Due Date</label>
                  <input type="date" value={newIssue.due_date} onChange={(e) => setNewIssue({ ...newIssue, due_date: e.target.value })} className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
              </div>
              <div className="flex gap-3 mt-4">
                <button type="submit" className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg">Create Issue</button>
                <button type="button" onClick={() => setShowCreate(false)} className="px-4 py-2 bg-slate-200 hover:bg-slate-300 text-slate-700 font-medium rounded-lg">Cancel</button>
              </div>
            </form>
          )}

          {/* Issues List */}
          <div className="space-y-3">
            {issues.length > 0 ? (
              issues.map((issue) => {
                const control = unifiedControls.find(c => c.id === issue.unified_control_id);
                return (
                  <div key={issue.id} className="border border-slate-200 rounded-lg p-4 hover:border-blue-300 transition-all" data-testid={`issue-${issue.id}`}>
                    <div className="flex items-start justify-between mb-3">
                      <div className="flex-1">
                        <div className="flex items-center gap-2 mb-2">
                          <h4 className="font-semibold text-slate-900">{issue.title}</h4>
                          <span className={`px-3 py-1 rounded-full text-xs font-semibold ${getSeverityColor(issue.severity)}`}>
                            {issue.severity}
                          </span>
                          <span className={`px-3 py-1 rounded-full text-xs font-semibold ${getStatusColor(issue.status)}`}>
                            {issue.status}
                          </span>
                          {issue.has_exception && (
                            <span className="px-3 py-1 bg-purple-100 text-purple-800 rounded-full text-xs font-semibold">
                              Exception
                            </span>
                          )}
                        </div>
                        <p className="text-sm text-slate-600 mb-2">{issue.description}</p>
                        {control && (
                          <div className="flex items-center gap-2 text-xs text-slate-500 mb-2">
                            <Shield className="h-3 w-3" />
                            <span>Control: <strong>{control.ccf_id} - {control.name}</strong></span>
                          </div>
                        )}
                        <div className="flex items-center gap-4 text-xs text-slate-500">
                          <span>Assigned: <strong>{issue.assigned_to}</strong></span>
                          {issue.due_date && <span>Due: <strong>{issue.due_date}</strong></span>}
                        </div>
                      </div>
                    </div>

                    {/* Actions */}
                    <div className="flex items-center gap-2 pt-3 border-t border-slate-200">
                      {issue.status === 'Open' && (
                        <button onClick={() => updateIssueStatus(issue.id, 'In Progress')} className="px-3 py-1 bg-yellow-600 hover:bg-yellow-700 text-white text-xs font-medium rounded-md">
                          Start Progress
                        </button>
                      )}
                      {issue.status === 'In Progress' && (
                        <button onClick={() => updateIssueStatus(issue.id, 'Resolved')} className="px-3 py-1 bg-green-600 hover:bg-green-700 text-white text-xs font-medium rounded-md">
                          Mark Resolved
                        </button>
                      )}
                      {issue.status === 'Resolved' && (
                        <button onClick={() => updateIssueStatus(issue.id, 'Closed')} className="px-3 py-1 bg-slate-600 hover:bg-slate-700 text-white text-xs font-medium rounded-md">
                          Close Issue
                        </button>
                      )}
                      {!issue.has_exception && issue.status !== 'Closed' && (
                        <button onClick={() => setSelectedIssue(issue)} className="px-3 py-1 bg-purple-600 hover:bg-purple-700 text-white text-xs font-medium rounded-md">
                          Add Exception
                        </button>
                      )}
                    </div>

                    {issue.has_exception && issue.exception_details && (
                      <div className="mt-3 p-3 bg-purple-50 border border-purple-200 rounded-lg">
                        <p className="text-xs font-semibold text-purple-900 mb-1">Exception Granted</p>
                        <p className="text-xs text-purple-800">Reason: {issue.exception_details.reason}</p>
                        <p className="text-xs text-purple-800">Approved by: {issue.exception_details.approved_by}</p>
                        {issue.exception_details.expiry_date && (
                          <p className="text-xs text-purple-800">Expires: {issue.exception_details.expiry_date}</p>
                        )}
                      </div>
                    )}
                  </div>
                );
              })
            ) : (
              <div className="text-center py-12 text-slate-500">
                <CheckCircle2 className="h-16 w-16 text-green-400 mx-auto mb-3" />
                <p className="text-lg font-medium">No issues</p>
                <p className="text-sm">All controls are passing</p>
              </div>
            )}
          </div>
        </div>

        {/* Exception Modal */}
        {selectedIssue && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
            <div className="bg-white rounded-lg max-w-lg w-full p-6">
              <h3 className="text-xl font-bold text-slate-900 mb-4">Add Exception</h3>
              <p className="text-sm text-slate-600 mb-4">Issue: <strong>{selectedIssue.title}</strong></p>
              
              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Exception Reason *</label>
                  <textarea
                    value={exceptionForm.reason}
                    onChange={(e) => setExceptionForm({ ...exceptionForm, reason: e.target.value })}
                    placeholder="Risk accepted due to..." rows={3} className="w-full px-3 py-2 border border-slate-300 rounded-md"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Approved By *</label>
                  <input type="text" value={exceptionForm.approved_by} onChange={(e) => setExceptionForm({ ...exceptionForm, approved_by: e.target.value })} placeholder="Senior Manager" className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Expiry Date</label>
                  <input type="date" value={exceptionForm.expiry_date} onChange={(e) => setExceptionForm({ ...exceptionForm, expiry_date: e.target.value })} className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
              </div>

              <div className="flex gap-3 mt-6">
                <button onClick={() => addException(selectedIssue.id)} className="flex-1 px-4 py-2 bg-purple-600 hover:bg-purple-700 text-white font-medium rounded-lg">Add Exception</button>
                <button onClick={() => setSelectedIssue(null)} className="px-4 py-2 bg-slate-200 hover:bg-slate-300 text-slate-700 font-medium rounded-lg">Cancel</button>
              </div>
            </div>
          </div>
        )}
      </motion.div>
    </div>
  );
};

export default IssueManagement;
