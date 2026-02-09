import React, { useContext, useState } from 'react';
import { AppContext } from '@/App';
import { motion } from 'framer-motion';
import axios from 'axios';
import { Shield, Check, X, Loader2, Info } from 'lucide-react';
import { toast } from 'sonner';

const FrameworkManagement = () => {
  const { frameworks, setFrameworks, refreshData, API } = useContext(AppContext);
  const [toggling, setToggling] = useState(null);

  const toggleFramework = async (frameworkId, currentStatus) => {
    setToggling(frameworkId);
    try {
      await axios.patch(`${API}/frameworks/${frameworkId}/toggle?enabled=${!currentStatus}`);
      
      // Update local state
      setFrameworks(frameworks.map(fw => 
        fw.id === frameworkId ? { ...fw, enabled: !currentStatus } : fw
      ));
      
      toast.success(!currentStatus ? 'Framework enabled' : 'Framework disabled');
    } catch (error) {
      console.error('Error toggling framework:', error);
      toast.error('Failed to update framework');
    } finally {
      setToggling(null);
    }
  };

  const enabledCount = frameworks.filter(f => f.enabled).length;
  const totalControls = frameworks
    .filter(f => f.enabled)
    .reduce((sum, f) => sum + f.total_controls, 0);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <div className="mb-8">
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-slate-900 mb-2">Framework Management</h1>
          <p className="text-lg text-slate-600">Select compliance frameworks to map and manage</p>
        </div>

        {/* Summary Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Enabled Frameworks</p>
            <p className="text-3xl font-bold text-slate-900">{enabledCount}</p>
            <p className="text-xs text-slate-600 mt-2">of {frameworks.length} available</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Total Controls</p>
            <p className="text-3xl font-bold text-slate-900">{totalControls}</p>
            <p className="text-xs text-slate-600 mt-2">from enabled frameworks</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Coverage</p>
            <p className="text-3xl font-bold text-slate-900">{((enabledCount / frameworks.length) * 100).toFixed(0)}%</p>
            <p className="text-xs text-slate-600 mt-2">framework coverage</p>
          </div>
        </div>

        {/* Info Banner */}
        <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-6 flex items-start gap-3">
          <Info className="h-5 w-5 text-blue-600 mt-0.5 flex-shrink-0" />
          <div>
            <h3 className="text-sm font-semibold text-blue-900 mb-1">Map Once, Comply Many</h3>
            <p className="text-sm text-blue-800">
              Enable the frameworks your organization needs to comply with. You'll create unified controls once, and automatically map them to all enabled frameworks - reducing duplication and ensuring consistency.
            </p>
          </div>
        </div>

        {/* Framework Cards */}
        <div className="space-y-4">
          {frameworks.map((framework, idx) => (
            <motion.div
              key={framework.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: idx * 0.1 }}
              className={`bg-white rounded-lg border-2 shadow-sm p-6 transition-all duration-200 ${
                framework.enabled 
                  ? 'border-blue-300 ring-2 ring-blue-100' 
                  : 'border-slate-200 hover:border-slate-300'
              }`}
              data-testid={`framework-${framework.id}`}
            >
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <div className="flex items-center gap-3 mb-2">
                    <div className={`h-12 w-12 rounded-lg flex items-center justify-center ${
                      framework.enabled ? 'bg-blue-100' : 'bg-slate-100'
                    }`}>
                      <Shield className={`h-6 w-6 ${
                        framework.enabled ? 'text-blue-600' : 'text-slate-600'
                      }`} />
                    </div>
                    <div>
                      <h3 className="text-xl font-bold text-slate-900">{framework.name}</h3>
                      <p className="text-sm text-slate-600">Version {framework.version}</p>
                    </div>
                    {framework.enabled && (
                      <div className="px-3 py-1 bg-green-100 text-green-800 rounded-full text-xs font-semibold">
                        Enabled
                      </div>
                    )}
                  </div>
                  
                  <p className="text-slate-700 mb-4">{framework.description}</p>
                  
                  <div className="flex items-center gap-4 text-sm text-slate-600">
                    <div className="flex items-center gap-1">
                      <span className="font-semibold text-slate-900">{framework.total_controls}</span>
                      <span>controls</span>
                    </div>
                  </div>
                </div>

                <button
                  onClick={() => toggleFramework(framework.id, framework.enabled)}
                  disabled={toggling === framework.id}
                  data-testid={`toggle-${framework.id}`}
                  className={`flex items-center gap-2 px-6 py-3 rounded-lg font-medium transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed ${
                    framework.enabled
                      ? 'bg-red-600 hover:bg-red-700 text-white'
                      : 'bg-blue-600 hover:bg-blue-700 text-white'
                  }`}
                >
                  {toggling === framework.id ? (
                    <>
                      <Loader2 className="h-5 w-5 animate-spin" />
                      <span>Processing...</span>
                    </>
                  ) : framework.enabled ? (
                    <>
                      <X className="h-5 w-5" />
                      <span>Disable</span>
                    </>
                  ) : (
                    <>
                      <Check className="h-5 w-5" />
                      <span>Enable</span>
                    </>
                  )}
                </button>
              </div>

              {framework.enabled && (
                <div className="mt-4 pt-4 border-t border-slate-200">
                  <p className="text-sm text-slate-600">
                    <strong>Next step:</strong> Go to Control Mapping to map {framework.name} controls to your unified control framework
                  </p>
                </div>
              )}
            </motion.div>
          ))}
        </div>

        {enabledCount === 0 && (
          <div className="mt-6 bg-amber-50 border border-amber-200 rounded-lg p-4">
            <p className="text-sm text-amber-800">
              <strong>Getting Started:</strong> Enable at least one framework to begin your GRC journey. We recommend starting with ISO 27001 or SOC 2.
            </p>
          </div>
        )}
      </motion.div>
    </div>
  );
};

export default FrameworkManagement;
