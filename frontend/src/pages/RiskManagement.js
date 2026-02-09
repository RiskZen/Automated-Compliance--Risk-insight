import React, { useContext, useState } from 'react';
import { AppContext } from '@/App';
import { motion } from 'framer-motion';
import axios from 'axios';
import { TrendingUp, Plus, Loader2, Brain, Sparkles } from 'lucide-react';
import { toast } from 'sonner';

const RiskManagement = () => {
  const { risks, setRisks, unifiedControls, kris, loading, API, refreshData } = useContext(AppContext);
  const [showCreate, setShowCreate] = useState(false);
  const [showAISuggestions, setShowAISuggestions] = useState(false);
  const [aiSuggestions, setAiSuggestions] = useState([]);
  const [loadingAI, setLoadingAI] = useState(false);
  const [newRisk, setNewRisk] = useState({
    name: '',
    description: '',
    category: 'Operational',
    inherent_risk_score: 5.0,
    residual_risk_score: 3.0,
    owner: '',
  });

  const getAISuggestions = async (industry = 'General') => {
    setLoadingAI(true);
    try {
      const response = await axios.post(`${API}/risks/ai-suggest?industry=${industry}`);
      if (response.data.risks) {
        setAiSuggestions(response.data.risks);
        setShowAISuggestions(true);
        toast.success('AI suggestions generated');
      }
    } catch (error) {
      console.error('Error getting AI suggestions:', error);
      toast.error('Failed to get AI suggestions');
    } finally {
      setLoadingAI(false);
    }
  };

  const applyAISuggestion = (suggestion) => {
    setNewRisk({
      name: suggestion.name,
      description: suggestion.description,
      category: suggestion.category,
      inherent_risk_score: suggestion.inherent_score,
      residual_risk_score: suggestion.inherent_score * 0.6,
      owner: '',
    });
    setShowAISuggestions(false);
    setShowCreate(true);
  };

  const createRisk = async (e) => {
    e.preventDefault();
    try {
      await axios.post(`${API}/risks`, {
        ...newRisk,
        kri_ids: [],
        linked_control_ids: [],
      });
      toast.success('Risk created');
      setShowCreate(false);
      setNewRisk({ name: '', description: '', category: 'Operational', inherent_risk_score: 5.0, residual_risk_score: 3.0, owner: '' });
      refreshData();
    } catch (error) {
      console.error('Error creating risk:', error);
      toast.error('Failed to create risk');
    }
  };

  const getRiskColor = (score) => {
    if (score >= 7) return 'text-red-600';
    if (score >= 4) return 'text-yellow-600';
    return 'text-green-600';
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
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-slate-900 mb-2">Risk Management</h1>
          <p className="text-lg text-slate-600">Manage risks with AI-powered insights</p>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-6">
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Total Risks</p>
            <p className="text-3xl font-bold text-slate-900">{risks.length}</p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Avg Inherent Risk</p>
            <p className="text-3xl font-bold text-red-600">
              {risks.length > 0 ? (risks.reduce((sum, r) => sum + r.inherent_risk_score, 0) / risks.length).toFixed(1) : '0.0'}
            </p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Avg Residual Risk</p>
            <p className="text-3xl font-bold text-green-600">
              {risks.length > 0 ? (risks.reduce((sum, r) => sum + r.residual_risk_score, 0) / risks.length).toFixed(1) : '0.0'}
            </p>
          </div>
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
            <p className="text-sm text-slate-500 mb-1">Risk Reduction</p>
            <p className="text-3xl font-bold text-blue-600">
              {risks.length > 0 ? (
                ((risks.reduce((sum, r) => sum + (r.inherent_risk_score - r.residual_risk_score), 0) / risks.reduce((sum, r) => sum + r.inherent_risk_score, 0)) * 100).toFixed(0)
              ) : '0'}%
            </p>
          </div>
        </div>

        {/* AI Suggestions Banner */}
        <div className="bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg p-6 mb-6 text-white">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <Sparkles className="h-8 w-8" />
              <div>
                <h3 className="text-xl font-bold mb-1">AI-Powered Risk Suggestions</h3>
                <p className="text-sm text-blue-100">Let AI suggest top 10 risks based on your industry</p>
              </div>
            </div>
            <button
              onClick={() => getAISuggestions('General')}
              disabled={loadingAI}
              className="flex items-center gap-2 px-6 py-3 bg-white text-blue-600 font-medium rounded-lg hover:bg-blue-50 transition-colors disabled:opacity-50"
            >
              {loadingAI ? (
                <>
                  <Loader2 className="h-5 w-5 animate-spin" />
                  Generating...
                </>
              ) : (
                <>
                  <Brain className="h-5 w-5" />
                  Get AI Suggestions
                </>
              )}
            </button>
          </div>
        </div>

        {/* AI Suggestions Modal */}
        {showAISuggestions && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
            <div className="bg-white rounded-lg max-w-4xl w-full max-h-[90vh] overflow-y-auto p-6">
              <h3 className="text-2xl font-bold text-slate-900 mb-4">AI-Suggested Risks</h3>
              <div className="space-y-3 mb-6">
                {aiSuggestions.map((suggestion, idx) => (
                  <div key={idx} className="border border-slate-200 rounded-lg p-4 hover:border-blue-300 transition-all">
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <h4 className="font-semibold text-slate-900 mb-1">{suggestion.name}</h4>
                        <p className="text-sm text-slate-600 mb-2">{suggestion.description}</p>
                        <div className="flex items-center gap-4 text-xs text-slate-500">
                          <span>Category: <strong>{suggestion.category}</strong></span>
                          <span>Inherent Score: <strong className={getRiskColor(suggestion.inherent_score)}>{suggestion.inherent_score}</strong></span>
                        </div>
                      </div>
                      <button
                        onClick={() => useAISuggestion(suggestion)}
                        className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium rounded-lg"
                      >
                        Use This
                      </button>
                    </div>
                  </div>
                ))}
              </div>
              <button
                onClick={() => setShowAISuggestions(false)}
                className="w-full px-4 py-2 bg-slate-200 hover:bg-slate-300 text-slate-700 font-medium rounded-lg"
              >
                Close
              </button>
            </div>
          </div>
        )}

        {/* Create Risk */}
        <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-xl font-semibold text-slate-900">Risks</h3>
            <button
              onClick={() => setShowCreate(!showCreate)}
              className="flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg"
            >
              <Plus className="h-5 w-5" />
              Add Risk
            </button>
          </div>

          {showCreate && (
            <form onSubmit={createRisk} className="bg-slate-50 rounded-lg p-4 mb-4">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="md:col-span-2">
                  <label className="block text-sm font-medium text-slate-700 mb-1">Risk Name *</label>
                  <input type="text" value={newRisk.name} onChange={(e) => setNewRisk({ ...newRisk, name: e.target.value })} placeholder="Data Breach" required className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div className="md:col-span-2">
                  <label className="block text-sm font-medium text-slate-700 mb-1">Description *</label>
                  <textarea value={newRisk.description} onChange={(e) => setNewRisk({ ...newRisk, description: e.target.value })} placeholder="Unauthorized access to sensitive data..." required rows={3} className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Category *</label>
                  <select value={newRisk.category} onChange={(e) => setNewRisk({ ...newRisk, category: e.target.value })} className="w-full px-3 py-2 border border-slate-300 rounded-md">
                    <option>Operational</option>
                    <option>Cybersecurity</option>
                    <option>Compliance</option>
                    <option>Financial</option>
                    <option>Strategic</option>
                    <option>Privacy</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Owner *</label>
                  <input type="text" value={newRisk.owner} onChange={(e) => setNewRisk({ ...newRisk, owner: e.target.value })} placeholder="CISO" required className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Inherent Risk Score (1-10) *</label>
                  <input type="number" step="0.1" min="1" max="10" value={newRisk.inherent_risk_score} onChange={(e) => setNewRisk({ ...newRisk, inherent_risk_score: parseFloat(e.target.value) })} required className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Residual Risk Score (1-10) *</label>
                  <input type="number" step="0.1" min="1" max="10" value={newRisk.residual_risk_score} onChange={(e) => setNewRisk({ ...newRisk, residual_risk_score: parseFloat(e.target.value) })} required className="w-full px-3 py-2 border border-slate-300 rounded-md" />
                </div>
              </div>
              <div className="flex gap-3 mt-4">
                <button type="submit" className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg">Create Risk</button>
                <button type="button" onClick={() => setShowCreate(false)} className="px-4 py-2 bg-slate-200 hover:bg-slate-300 text-slate-700 font-medium rounded-lg">Cancel</button>
              </div>
            </form>
          )}

          {/* Risks List */}
          <div className="space-y-3">
            {risks.map((risk) => {
              const linkedKRIs = kris.filter(k => k.risk_id === risk.id);
              const linkedControls = unifiedControls.filter(c => risk.linked_control_ids?.includes(c.id));
              
              return (
                <div key={risk.id} className="border border-slate-200 rounded-lg p-4 hover:border-blue-300 transition-all">
                  <div className="flex items-start justify-between mb-3">
                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2">
                        <h4 className="font-semibold text-slate-900 text-lg">{risk.name}</h4>
                        <span className="px-2 py-1 bg-slate-100 text-slate-700 rounded text-xs font-semibold">{risk.category}</span>
                      </div>
                      <p className="text-sm text-slate-600 mb-3">{risk.description}</p>
                      
                      <div className="grid grid-cols-2 md:grid-cols-5 gap-4 mb-2">
                        <div>
                          <p className="text-xs text-slate-500">Inherent Risk</p>
                          <p className={`text-lg font-bold ${getRiskColor(risk.inherent_risk_score)}`}>{risk.inherent_risk_score.toFixed(1)}</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">Residual Risk</p>
                          <p className={`text-lg font-bold ${getRiskColor(risk.residual_risk_score)}`}>{risk.residual_risk_score.toFixed(1)}</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">Reduction</p>
                          <p className="text-lg font-bold text-green-600">
                            {((risk.inherent_risk_score - risk.residual_risk_score) / risk.inherent_risk_score * 100).toFixed(0)}%
                          </p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">KRIs</p>
                          <p className="text-lg font-bold text-blue-600">{linkedKRIs.length}</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">Controls</p>
                          <p className="text-lg font-bold text-slate-900">{linkedControls.length}</p>
                        </div>
                      </div>
                      
                      <div className="text-xs text-slate-500">
                        Owner: <strong>{risk.owner}</strong>
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

export default RiskManagement;
