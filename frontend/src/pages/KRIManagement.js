import React, { useContext, useState } from 'react';
import { AppContext } from '@/App';
import { motion } from 'framer-motion';
import axios from 'axios';
import { BarChart3, Plus, Loader2, TrendingUp, AlertTriangle } from 'lucide-react';
import { toast } from 'sonner';

const KRIManagement = () => {
  const { risks, kris, loading, API, refreshData } = useContext(AppContext);
  const [showCreate, setShowCreate] = useState(false);
  const [newKRI, setNewKRI] = useState({
    name: '',
    description: '',
    risk_id: '',
    current_value: 0,
    threshold: 100,
    unit: 'count',
    status: 'Normal',
    trend: 'Stable',
  });

  const createKRI = async (e) => {
    e.preventDefault();
    try {
      await axios.post(`${API}/kris`, { ...newKRI, kci_ids: [] });
      toast.success('KRI created');
      setShowCreate(false);
      setNewKRI({ name: '', description: '', risk_id: '', current_value: 0, threshold: 100, unit: 'count', status: 'Normal', trend: 'Stable' });
      refreshData();
    } catch (error) {
      console.error('Error creating KRI:', error);
      toast.error('Failed to create KRI');
    }
  };

  const getStatusColor = (status) => {
    switch (status) {
      case 'Normal': return 'bg-green-100 text-green-800';
      case 'Warning': return 'bg-yellow-100 text-yellow-800';
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
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-slate-900 mb-2">KRI Management</h1>
          <p className="text-lg text-slate-600">Key Risk Indicators - Monitor risk levels in real-time</p>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-6">
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Total KRIs</p>
            <p className="text-3xl font-bold text-slate-900">{kris.length}</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Normal</p>
            <p className="text-3xl font-bold text-green-600">{kris.filter(k => k.status === 'Normal').length}</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Warning</p>
            <p className="text-3xl font-bold text-yellow-600">{kris.filter(k => k.status === 'Warning').length}</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Critical</p>
            <p className="text-3xl font-bold text-red-600">{kris.filter(k => k.status === 'Critical').length}</p>
          </div>
        </div>

        {/* Create KRI */}
        <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-xl font-semibold text-slate-900">Key Risk Indicators</h3>
            <button
              onClick={() => setShowCreate(!showCreate)}
              className="flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg"
            >
              <Plus className="h-5 w-5" />
              Create KRI
            </button>
          </div>

          {showCreate && (
            <form onSubmit={createKRI} className="bg-slate-50 rounded-lg p-4 mb-4">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="md:col-span-2">
                  <label className="block text-sm font-medium text-slate-700 mb-1">KRI Name *</label>
                  <input type="text" value={newKRI.name} onChange={(e) => setNewKRI({ ...newKRI, name: e.target.value })} placeholder="Failed Login Attempts" required className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div className="md:col-span-2">
                  <label className="block text-sm font-medium text-slate-700 mb-1">Description *</label>
                  <textarea value={newKRI.description} onChange={(e) => setNewKRI({ ...newKRI, description: e.target.value })} placeholder="Number of failed login attempts per hour..." required rows={3} className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Linked Risk *</label>
                  <select value={newKRI.risk_id} onChange={(e) => setNewKRI({ ...newKRI, risk_id: e.target.value })} required className="w-full px-3 py-2 border border-slate-300 rounded-md">
                    <option value="">Select risk...</option>
                    {risks.map(r => (
                      <option key={r.id} value={r.id}>{r.name}</option>
                    ))}
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Unit *</label>
                  <input type="text" value={newKRI.unit} onChange={(e) => setNewKRI({ ...newKRI, unit: e.target.value })} placeholder="count, %, score" required className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Current Value *</label>
                  <input type="number" step="0.1" value={newKRI.current_value} onChange={(e) => setNewKRI({ ...newKRI, current_value: parseFloat(e.target.value) })} required className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Threshold *</label>
                  <input type="number" step="0.1" value={newKRI.threshold} onChange={(e) => setNewKRI({ ...newKRI, threshold: parseFloat(e.target.value) })} required className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Status *</label>
                  <select value={newKRI.status} onChange={(e) => setNewKRI({ ...newKRI, status: e.target.value })} className="w-full px-3 py-2 border border-slate-300 rounded-md">
                    <option>Normal</option>
                    <option>Warning</option>
                    <option>Critical</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Trend *</label>
                  <select value={newKRI.trend} onChange={(e) => setNewKRI({ ...newKRI, trend: e.target.value })} className="w-full px-3 py-2 border border-slate-300 rounded-md">
                    <option>Stable</option>
                    <option>Increasing</option>
                    <option>Decreasing</option>
                  </select>
                </div>
              </div>
              <div className="flex gap-3 mt-4">
                <button type="submit" className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg">Create KRI</button>
                <button type="button" onClick={() => setShowCreate(false)} className="px-4 py-2 bg-slate-200 hover:bg-slate-300 text-slate-700 font-medium rounded-lg">Cancel</button>
              </div>
            </form>
          )}

          {/* KRIs List */}
          <div className="space-y-3">
            {kris.map((kri) => {
              const risk = risks.find(r => r.id === kri.risk_id);
              const utilizationPercent = (kri.current_value / kri.threshold * 100).toFixed(0);
              
              return (
                <div key={kri.id} className="border border-slate-200 rounded-lg p-4 hover:border-blue-300 transition-all">
                  <div className="flex items-start justify-between mb-3">
                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2">
                        <h4 className="font-semibold text-slate-900">{kri.name}</h4>
                        <span className={`px-3 py-1 rounded-full text-xs font-semibold ${getStatusColor(kri.status)}`}>
                          {kri.status}
                        </span>
                      </div>
                      <p className="text-sm text-slate-600 mb-3">{kri.description}</p>
                      
                      {risk && (
                        <div className="flex items-center gap-2 text-xs text-slate-500 mb-3">
                          <AlertTriangle className="h-3 w-3" />
                          <span>Risk: <strong>{risk.name}</strong></span>
                        </div>
                      )}
                      
                      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                        <div>
                          <p className="text-xs text-slate-500">Current Value</p>
                          <p className="text-lg font-bold text-slate-900">{kri.current_value} {kri.unit}</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">Threshold</p>
                          <p className="text-lg font-bold text-slate-900">{kri.threshold} {kri.unit}</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">Utilization</p>
                          <p className={`text-lg font-bold ${
                            utilizationPercent >= 90 ? 'text-red-600' :
                            utilizationPercent >= 70 ? 'text-yellow-600' : 'text-green-600'
                          }`}>{utilizationPercent}%</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">Trend</p>
                          <div className="flex items-center gap-1">
                            {kri.trend === 'Increasing' && <TrendingUp className="h-4 w-4 text-red-600" />}
                            {kri.trend === 'Decreasing' && <TrendingUp className="h-4 w-4 text-green-600 rotate-180" />}
                            <p className="text-sm font-medium text-slate-900">{kri.trend}</p>
                          </div>
                        </div>
                      </div>
                      
                      {/* Progress Bar */}
                      <div className="mt-3">
                        <div className="w-full bg-slate-200 rounded-full h-2">
                          <div
                            className={`h-2 rounded-full ${
                              utilizationPercent >= 90 ? 'bg-red-600' :
                              utilizationPercent >= 70 ? 'bg-yellow-600' : 'bg-green-600'
                            }`}
                            style={{ width: `${Math.min(utilizationPercent, 100)}%` }}
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

export default KRIManagement;
