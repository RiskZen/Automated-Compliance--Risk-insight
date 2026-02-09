import React, { useContext, useState } from 'react';
import { AppContext } from '@/App';
import { motion } from 'framer-motion';
import axios from 'axios';
import { FileText, Plus, Loader2 } from 'lucide-react';
import { toast } from 'sonner';

const PolicyManagement = () => {
  const { policies, setPolicies, loading, API, refreshData } = useContext(AppContext);
  const [showCreate, setShowCreate] = useState(false);
  const [newPolicy, setNewPolicy] = useState({
    policy_id: '',
    name: '',
    description: '',
    category: 'Security',
    owner: '',
  });

  const createPolicy = async (e) => {
    e.preventDefault();
    try {
      await axios.post(`${API}/policies`, newPolicy);
      toast.success('Policy created');
      setShowCreate(false);
      setNewPolicy({ policy_id: '', name: '', description: '', category: 'Security', owner: '' });
      refreshData();
    } catch (error) {
      console.error('Error creating policy:', error);
      toast.error('Failed to create policy');
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
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-slate-900 mb-2">Policy Management</h1>
          <p className="text-lg text-slate-600">Manage internal policies and map to controls</p>
        </div>

        <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-xl font-semibold text-slate-900">Internal Policies</h3>
            <button
              onClick={() => setShowCreate(!showCreate)}
              className="flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition-colors"
            >
              <Plus className="h-5 w-5" />
              Create Policy
            </button>
          </div>

          {showCreate && (
            <form onSubmit={createPolicy} className="bg-slate-50 rounded-lg p-4 mb-4">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Policy ID *</label>
                  <input type="text" value={newPolicy.policy_id} onChange={(e) => setNewPolicy({ ...newPolicy, policy_id: e.target.value })} placeholder="POL-SEC-100" required className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Policy Name *</label>
                  <input type="text" value={newPolicy.name} onChange={(e) => setNewPolicy({ ...newPolicy, name: e.target.value })} placeholder="Information Security Policy" required className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div className="md:col-span-2">
                  <label className="block text-sm font-medium text-slate-700 mb-1">Description *</label>
                  <textarea value={newPolicy.description} onChange={(e) => setNewPolicy({ ...newPolicy, description: e.target.value })} placeholder="Master policy governing..." required rows={3} className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Category *</label>
                  <select value={newPolicy.category} onChange={(e) => setNewPolicy({ ...newPolicy, category: e.target.value })} className="w-full px-3 py-2 border border-slate-300 rounded-md">
                    <option>Security</option>
                    <option>Data Protection</option>
                    <option>Access Control</option>
                    <option>Monitoring</option>
                    <option>Business Continuity</option>
                    <option>Network Security</option>
                    <option>Privacy</option>
                    <option>Change Management</option>
                    <option>Incident Management</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Owner *</label>
                  <input type="text" value={newPolicy.owner} onChange={(e) => setNewPolicy({ ...newPolicy, owner: e.target.value })} placeholder="CISO" required className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
              </div>
              <div className="flex gap-3 mt-4">
                <button type="submit" className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg">Create Policy</button>
                <button type="button" onClick={() => setShowCreate(false)} className="px-4 py-2 bg-slate-200 hover:bg-slate-300 text-slate-700 font-medium rounded-lg">Cancel</button>
              </div>
            </form>
          )}

          <div className="space-y-3">
            {policies.map((policy) => (
              <div key={policy.id} className="border border-slate-200 rounded-lg p-4 hover:border-blue-300 transition-all">
                <div className="flex items-start justify-between">
                  <div className="flex-1">
                    <div className="flex items-center gap-3 mb-2">
                      <div className="px-2 py-1 bg-purple-100 text-purple-800 rounded text-xs font-mono font-semibold">{policy.policy_id}</div>
                      <h4 className="font-semibold text-slate-900">{policy.name}</h4>
                      <span className="px-2 py-0.5 bg-green-100 text-green-800 text-xs rounded-full font-semibold">{policy.status}</span>
                    </div>
                    <p className="text-sm text-slate-600 mb-2">{policy.description}</p>
                    <div className="flex items-center gap-4 text-xs text-slate-500">
                      <span>Category: <strong>{policy.category}</strong></span>
                      <span>Owner: <strong>{policy.owner}</strong></span>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default PolicyManagement;
