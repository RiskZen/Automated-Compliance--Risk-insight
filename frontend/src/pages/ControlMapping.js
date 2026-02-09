import React, { useContext, useState, useEffect } from 'react';
import { AppContext } from '@/App';
import { motion } from 'framer-motion';
import axios from 'axios';
import { GitBranch, Shield, FileText, Link2, Plus, Loader2, CheckCircle2, Info } from 'lucide-react';
import { toast } from 'sonner';

const ControlMapping = () => {
  const { frameworks, unifiedControls, policies, loading, API, refreshData } = useContext(AppContext);
  const [selectedControl, setSelectedControl] = useState(null);
  const [frameworkControls, setFrameworkControls] = useState([]);
  const [loadingFrameworkControls, setLoadingFrameworkControls] = useState(false);
  const [showCreateControl, setShowCreateControl] = useState(false);
  const [newControl, setNewControl] = useState({
    ccf_id: '',
    name: '',
    description: '',
    control_type: 'Preventive',
    frequency: 'Continuous',
    owner: '',
  });

  const enabledFrameworks = frameworks.filter(f => f.enabled);

  useEffect(() => {
    if (enabledFrameworks.length > 0) {
      loadFrameworkControls();
    }
  }, [enabledFrameworks.length]);

  const loadFrameworkControls = async () => {
    setLoadingFrameworkControls(true);
    try {
      const allControls = [];
      for (const fw of enabledFrameworks) {
        const response = await axios.get(`${API}/framework-controls/${fw.id}`);
        allControls.push(...response.data.map(c => ({ ...c, framework_name: fw.name })));
      }
      setFrameworkControls(allControls);
    } catch (error) {
      console.error('Error loading framework controls:', error);
      toast.error('Failed to load framework controls');
    } finally {
      setLoadingFrameworkControls(false);
    }
  };

  const createUnifiedControl = async (e) => {
    e.preventDefault();
    try {
      await axios.post(`${API}/unified-controls`, {
        ...newControl,
        mapped_framework_controls: [],
        mapped_policies: [],
        automation_possible: false,
      });
      toast.success('Unified control created');
      setShowCreateControl(false);
      setNewControl({
        ccf_id: '',
        name: '',
        description: '',
        control_type: 'Preventive',
        frequency: 'Continuous',
        owner: '',
      });
      refreshData();
    } catch (error) {
      console.error('Error creating control:', error);
      toast.error('Failed to create control');
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <Loader2 className="h-12 w-12 text-blue-500 animate-spin" />
      </div>
    );
  }

  if (enabledFrameworks.length === 0) {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-8">
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-slate-900 mb-2">Control Mapping</h1>
          <p className="text-lg text-slate-600">Map framework controls to unified CCF controls and internal policies</p>
        </div>

        <div className="bg-amber-50 border border-amber-200 rounded-lg p-8 text-center">
          <Shield className="h-16 w-16 text-amber-500 mx-auto mb-4" />
          <h3 className="text-xl font-bold text-slate-900 mb-2">No Frameworks Enabled</h3>
          <p className="text-slate-600 mb-4">
            You need to enable at least one compliance framework before you can map controls.
          </p>
          <a
            href="/frameworks"
            className="inline-flex items-center gap-2 px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition-colors"
          >
            Go to Framework Management
          </a>
        </div>
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
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-slate-900 mb-2">Control Mapping</h1>
          <p className="text-lg text-slate-600">Map framework controls → Unified CCF → Internal policies</p>
        </div>

        {/* Info Banner */}
        <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-6 flex items-start gap-3">
          <Info className="h-5 w-5 text-blue-600 mt-0.5 flex-shrink-0" />
          <div>
            <h3 className="text-sm font-semibold text-blue-900 mb-1">Map Once, Comply Many</h3>
            <p className="text-sm text-blue-800">
              Create unified controls once, then map them to multiple framework requirements. This eliminates duplication and ensures consistent implementation across all compliance frameworks.
            </p>
          </div>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-6">
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Enabled Frameworks</p>
            <p className="text-3xl font-bold text-slate-900">{enabledFrameworks.length}</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Framework Controls</p>
            <p className="text-3xl font-bold text-slate-900">{frameworkControls.length}</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Unified Controls</p>
            <p className="text-3xl font-bold text-slate-900">{unifiedControls.length}</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Internal Policies</p>
            <p className="text-3xl font-bold text-slate-900">{policies.length}</p>
          </div>
        </div>

        {/* Create Unified Control */}
        <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6 mb-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-xl font-semibold text-slate-900">Unified Controls (CCF)</h3>
            <button
              onClick={() => setShowCreateControl(!showCreateControl)}
              className="flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition-colors"
              data-testid="create-control-btn"
            >
              <Plus className="h-5 w-5" />
              Create Unified Control
            </button>
          </div>

          {showCreateControl && (
            <form onSubmit={createUnifiedControl} className="bg-slate-50 rounded-lg p-4 mb-4">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">CCF ID *</label>
                  <input
                    type="text"
                    value={newControl.ccf_id}
                    onChange={(e) => setNewControl({ ...newControl, ccf_id: e.target.value })}
                    placeholder="CCF-AC-001"
                    required
                    className="w-full px-3 py-2 border border-slate-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Control Name *</label>
                  <input
                    type="text"
                    value={newControl.name}
                    onChange={(e) => setNewControl({ ...newControl, name: e.target.value })}
                    placeholder="Multi-Factor Authentication"
                    required
                    className="w-full px-3 py-2 border border-slate-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
                <div className="md:col-span-2">
                  <label className="block text-sm font-medium text-slate-700 mb-1">Description *</label>
                  <textarea
                    value={newControl.description}
                    onChange={(e) => setNewControl({ ...newControl, description: e.target.value })}
                    placeholder="Enforce MFA for all user accounts..."
                    required
                    rows={3}
                    className="w-full px-3 py-2 border border-slate-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Control Type *</label>
                  <select
                    value={newControl.control_type}
                    onChange={(e) => setNewControl({ ...newControl, control_type: e.target.value })}
                    className="w-full px-3 py-2 border border-slate-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option>Preventive</option>
                    <option>Detective</option>
                    <option>Corrective</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Frequency *</label>
                  <select
                    value={newControl.frequency}
                    onChange={(e) => setNewControl({ ...newControl, frequency: e.target.value })}
                    className="w-full px-3 py-2 border border-slate-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option>Continuous</option>
                    <option>Daily</option>
                    <option>Weekly</option>
                    <option>Monthly</option>
                    <option>Quarterly</option>
                    <option>Annual</option>
                    <option>As Needed</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Owner *</label>
                  <input
                    type="text"
                    value={newControl.owner}
                    onChange={(e) => setNewControl({ ...newControl, owner: e.target.value })}
                    placeholder="IT Security Team"
                    required
                    className="w-full px-3 py-2 border border-slate-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
              </div>
              <div className="flex gap-3 mt-4">
                <button
                  type="submit"
                  className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition-colors"
                >
                  Create Control
                </button>
                <button
                  type="button"
                  onClick={() => setShowCreateControl(false)}
                  className="px-4 py-2 bg-slate-200 hover:bg-slate-300 text-slate-700 font-medium rounded-lg transition-colors"
                >
                  Cancel
                </button>
              </div>
            </form>
          )}

          {/* Unified Controls List */}
          <div className="space-y-3">
            {unifiedControls.length > 0 ? (
              unifiedControls.map((control) => (
                <div
                  key={control.id}
                  className="border border-slate-200 rounded-lg p-4 hover:border-blue-300 hover:shadow-md transition-all duration-200"
                  data-testid={`unified-control-${control.id}`}
                >
                  <div className="flex items-start justify-between">
                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2">
                        <div className="px-2 py-1 bg-blue-100 text-blue-800 rounded text-xs font-mono font-semibold">
                          {control.ccf_id}
                        </div>
                        <h4 className="font-semibold text-slate-900">{control.name}</h4>
                      </div>
                      <p className="text-sm text-slate-600 mb-3">{control.description}</p>
                      
                      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-3">
                        <div>
                          <p className="text-xs text-slate-500">Type</p>
                          <p className="text-sm font-medium text-slate-900">{control.control_type}</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">Frequency</p>
                          <p className="text-sm font-medium text-slate-900">{control.frequency}</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">Owner</p>
                          <p className="text-sm font-medium text-slate-900">{control.owner}</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">Mapped Controls</p>
                          <p className="text-sm font-bold text-blue-600">{control.mapped_framework_controls?.length || 0}</p>
                        </div>
                      </div>

                      {control.mapped_policies && control.mapped_policies.length > 0 && (
                        <div className="flex items-center gap-2 mb-2">
                          <FileText className="h-4 w-4 text-slate-500" />
                          <span className="text-xs text-slate-500">Policies:</span>
                          <div className="flex flex-wrap gap-1">
                            {control.mapped_policies.map(polId => {
                              const policy = policies.find(p => p.id === polId);
                              return policy ? (
                                <span key={polId} className="px-2 py-0.5 bg-purple-100 text-purple-800 text-xs rounded-full">
                                  {policy.policy_id}
                                </span>
                              ) : null;
                            })}
                          </div>
                        </div>
                      )}

                      {control.automation_possible && (
                        <div className="inline-flex items-center gap-1 px-2 py-1 bg-green-100 text-green-800 rounded text-xs font-semibold">
                          <CheckCircle2 className="h-3 w-3" />
                          Automation Possible
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              ))
            ) : (
              <div className="text-center py-8 text-slate-500">
                <Shield className="h-12 w-12 text-slate-300 mx-auto mb-3" />
                <p>No unified controls created yet</p>
                <p className="text-sm mt-1">Click "Create Unified Control" to get started</p>
              </div>
            )}
          </div>
        </div>

        {/* Framework Controls Reference */}
        <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
          <h3 className="text-xl font-semibold text-slate-900 mb-4">Framework Controls Reference</h3>
          <p className="text-sm text-slate-600 mb-4">
            These are the controls from your enabled frameworks. Map them to your unified controls above.
          </p>
          
          {loadingFrameworkControls ? (
            <div className="flex items-center justify-center py-8">
              <Loader2 className="h-8 w-8 text-blue-500 animate-spin" />
            </div>
          ) : frameworkControls.length > 0 ? (
            <div className="space-y-3 max-h-96 overflow-y-auto">
              {frameworkControls.map((control) => (
                <div
                  key={control.id}
                  className="border border-slate-200 rounded-lg p-4 hover:bg-slate-50 transition-colors"
                >
                  <div className="flex items-start gap-3">
                    <Shield className="h-5 w-5 text-slate-400 mt-1 flex-shrink-0" />
                    <div className="flex-1">
                      <div className="flex items-center gap-2 mb-1">
                        <span className="px-2 py-0.5 bg-slate-100 text-slate-700 text-xs font-mono rounded">
                          {control.control_id}
                        </span>
                        <span className="text-xs text-slate-500">{control.framework_name}</span>
                      </div>
                      <h4 className="font-medium text-slate-900 text-sm mb-1">{control.title}</h4>
                      <p className="text-xs text-slate-600">{control.description}</p>
                      {control.category && (
                        <span className="inline-block mt-2 px-2 py-0.5 bg-blue-50 text-blue-700 text-xs rounded">
                          {control.category}
                        </span>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="text-center py-8 text-slate-500">
              <p>No framework controls available</p>
            </div>
          )}
        </div>
      </motion.div>
    </div>
  );
};

export default ControlMapping;
