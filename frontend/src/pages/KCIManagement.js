import React, { useContext, useState } from 'react';
import { AppContext } from '@/App';
import { motion } from 'framer-motion';
import axios from 'axios';
import { Target, Plus, Loader2, CheckCircle2, AlertCircle } from 'lucide-react';
import { toast } from 'sonner';

const KCIManagement = () => {
  const { kcis, kris, unifiedControls, loading, API, refreshData } = useContext(AppContext);
  const [showCreate, setShowCreate] = useState(false);
  const [newKCI, setNewKCI] = useState({
    name: '',
    description: '',
    kri_id: '',
    unified_control_id: '',
    current_value: 0,
    target: 100,
    unit: '%',
    status: 'On Track',
  });

  const createKCI = async (e) => {
    e.preventDefault();
    try {
      await axios.post(`${API}/kcis`, newKCI);
      toast.success('KCI created');
      setShowCreate(false);
      setNewKCI({ name: '', description: '', kri_id: '', unified_control_id: '', current_value: 0, target: 100, unit: '%', status: 'On Track' });
      refreshData();
    } catch (error) {
      console.error('Error creating KCI:', error);
      toast.error('Failed to create KCI');
    }
  };

  const getStatusColor = (status) => {
    switch (status) {
      case 'Excellent': return 'bg-green-100 text-green-800';
      case 'On Track': return 'bg-blue-100 text-blue-800';
      case 'Needs Attention': return 'bg-yellow-100 text-yellow-800';
      case 'Critical': return 'bg-red-100 text-red-800';
      default: return 'bg-slate-100 text-slate-800';
    }
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
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-slate-900 mb-2">KCI Management</h1>
          <p className="text-lg text-slate-600">Key Control Indicators - Measure control effectiveness</p>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-6">
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Total KCIs</p>
            <p className="text-3xl font-bold text-slate-900">{kcis.length}</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">On Track</p>
            <p className="text-3xl font-bold text-blue-600">{kcis.filter(k => k.status === 'On Track' || k.status === 'Excellent').length}</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Needs Attention</p>
            <p className="text-3xl font-bold text-yellow-600">{kcis.filter(k => k.status === 'Needs Attention').length}</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Avg Performance</p>
            <p className="text-3xl font-bold text-green-600">
              {kcis.length > 0 ? (kcis.reduce((sum, k) => sum + (k.current_value / k.target * 100), 0) / kcis.length).toFixed(0) : 0}%
            </p>
          </div>
        </div>

        {/* Create KCI */}
        <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-xl font-semibold text-slate-900">Key Control Indicators</h3>
            <button
              onClick={() => setShowCreate(!showCreate)}
              className="flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg"
            >
              <Plus className="h-5 w-5" />
              Create KCI
            </button>
          </div>

          {showCreate && (
            <form onSubmit={createKCI} className="bg-slate-50 rounded-lg p-4 mb-4">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="md:col-span-2">
                  <label className="block text-sm font-medium text-slate-700 mb-1">KCI Name *</label>
                  <input type="text" value={newKCI.name} onChange={(e) => setNewKCI({ ...newKCI, name: e.target.value })} placeholder="MFA Adoption Rate" required className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div className="md:col-span-2">
                  <label className="block text-sm font-medium text-slate-700 mb-1">Description *</label>
                  <textarea value={newKCI.description} onChange={(e) => setNewKCI({ ...newKCI, description: e.target.value })} placeholder="Percentage of users with MFA enabled..." required rows={3} className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Linked KRI *</label>
                  <select value={newKCI.kri_id} onChange={(e) => setNewKCI({ ...newKCI, kri_id: e.target.value })} required className="w-full px-3 py-2 border border-slate-300 rounded-md">
                    <option value="">Select KRI...</option>
                    {kris.map(k => (
                      <option key={k.id} value={k.id}>{k.name}</option>
                    ))}
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Linked Control *</label>
                  <select value={newKCI.unified_control_id} onChange={(e) => setNewKCI({ ...newKCI, unified_control_id: e.target.value })} required className="w-full px-3 py-2 border border-slate-300 rounded-md">
                    <option value="">Select control...</option>
                    {unifiedControls.map(c => (
                      <option key={c.id} value={c.id}>{c.ccf_id} - {c.name}</option>
                    ))}
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Unit *</label>
                  <input type="text" value={newKCI.unit} onChange={(e) => setNewKCI({ ...newKCI, unit: e.target.value })} placeholder="%, count, score" required className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Status *</label>
                  <select value={newKCI.status} onChange={(e) => setNewKCI({ ...newKCI, status: e.target.value })} className="w-full px-3 py-2 border border-slate-300 rounded-md">
                    <option>Excellent</option>
                    <option>On Track</option>
                    <option>Needs Attention</option>
                    <option>Critical</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Current Value *</label>
                  <input type="number" step="0.1" value={newKCI.current_value} onChange={(e) => setNewKCI({ ...newKCI, current_value: parseFloat(e.target.value) })} required className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Target *</label>
                  <input type="number" step="0.1" value={newKCI.target} onChange={(e) => setNewKCI({ ...newKCI, target: parseFloat(e.target.value) })} required className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
              </div>
              <div className="flex gap-3 mt-4">
                <button type="submit" className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg">Create KCI</button>
                <button type="button" onClick={() => setShowCreate(false)} className="px-4 py-2 bg-slate-200 hover:bg-slate-300 text-slate-700 font-medium rounded-lg">Cancel</button>
              </div>
            </form>
          )}

          {/* KCIs List */}
          <div className="space-y-3">
            {kcis.map((kci) => {
              const kri = kris.find(k => k.id === kci.kri_id);
              const control = unifiedControls.find(c => c.id === kci.unified_control_id);
              const performancePercent = (kci.current_value / kci.target * 100).toFixed(0);
              
              return (
                <div key={kci.id} className="border border-slate-200 rounded-lg p-4 hover:border-blue-300 transition-all">
                  <div className="flex items-start justify-between mb-3">
                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2">
                        <h4 className="font-semibold text-slate-900">{kci.name}</h4>
                        <span className={`px-3 py-1 rounded-full text-xs font-semibold ${getStatusColor(kci.status)}`}>
                          {kci.status}
                        </span>
                      </div>
                      <p className="text-sm text-slate-600 mb-3">{kci.description}</p>
                      
                      <div className="flex flex-wrap items-center gap-4 text-xs text-slate-500 mb-3">
                        {kri && (
                          <span>KRI: <strong>{kri.name}</strong></span>
                        )}
                        {control && (
                          <span>Control: <strong>{control.ccf_id} - {control.name}</strong></span>
                        )}
                      </div>
                      
                      <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
                        <div>
                          <p className="text-xs text-slate-500">Current Value</p>
                          <p className="text-lg font-bold text-slate-900">{kci.current_value} {kci.unit}</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">Target</p>
                          <p className="text-lg font-bold text-slate-900">{kci.target} {kci.unit}</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">Performance</p>
                          <p className={`text-lg font-bold ${
                            performancePercent >= 90 ? 'text-green-600' :
                            performancePercent >= 70 ? 'text-blue-600' : 'text-yellow-600'
                          }`}>{performancePercent}%</p>
                        </div>
                      </div>
                      
                      {/* Progress Bar */}
                      <div className="mt-3">
                        <div className="w-full bg-slate-200 rounded-full h-2">
                          <div
                            className={`h-2 rounded-full ${
                              performancePercent >= 90 ? 'bg-green-600' :
                              performancePercent >= 70 ? 'bg-blue-600' : 'bg-yellow-600'
                            }`}
                            style={{ width: `${Math.min(performancePercent, 100)}%` }}
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default KCIManagement;
