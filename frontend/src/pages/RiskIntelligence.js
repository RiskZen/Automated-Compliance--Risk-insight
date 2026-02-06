import React, { useContext, useState } from 'react';
import { AppContext } from '@/App';
import { motion } from 'framer-motion';
import axios from 'axios';
import { Brain, TrendingUp, TrendingDown, Loader2, AlertTriangle, ArrowRight, Activity } from 'lucide-react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from 'recharts';
import { toast } from 'sonner';

const RiskIntelligence = () => {
  const { risks, controls, kris, kcis, loading, API } = useContext(AppContext);
  const [aiAnalysis, setAiAnalysis] = useState(null);
  const [analyzing, setAnalyzing] = useState(false);

  const topRisks = [...risks]
    .sort((a, b) => b.residual_risk_score - a.residual_risk_score)
    .slice(0, 10);

  const analyzeRiskKRIMapping = async (risk) => {
    setAnalyzing(true);
    try {
      const linkedKRIs = kris.filter(kri => risk.kris.includes(kri.id));
      const linkedControls = controls.filter(c => risk.linked_controls.includes(c.id));
      const linkedKCIs = kcis.filter(kci => linkedControls.some(c => c.id === kci.control_id));

      const context = {
        risk: {
          name: risk.name,
          description: risk.description,
          inherent_score: risk.inherent_risk_score,
          residual_score: risk.residual_risk_score,
          category: risk.category,
        },
        kris: linkedKRIs.map(k => ({
          name: k.name,
          current_value: k.current_value,
          threshold: k.threshold,
          status: k.status,
          trend: k.trend,
        })),
        controls: linkedControls.map(c => ({
          name: c.name,
          health_score: c.health_score,
          status: c.status,
        })),
        kcis: linkedKCIs.map(k => ({
          name: k.name,
          current_value: k.current_value,
          target: k.target,
          status: k.status,
        })),
      };

      const response = await axios.post(`${API}/ai/analyze`, {
        analysis_type: 'risk_kri_mapping',
        context,
      });

      setAiAnalysis({ riskName: risk.name, ...response.data });
      toast.success('AI analysis completed');
    } catch (error) {
      console.error('Error analyzing risk:', error);
      toast.error('Failed to generate AI analysis');
    } finally {
      setAnalyzing(false);
    }
  };

  const analyzeControlHealthImpact = async (risk) => {
    setAnalyzing(true);
    try {
      const linkedControls = controls.filter(c => risk.linked_controls.includes(c.id));
      const avgControlHealth = linkedControls.reduce((sum, c) => sum + c.health_score, 0) / linkedControls.length;

      const context = {
        risk: {
          name: risk.name,
          residual_score: risk.residual_risk_score,
          inherent_score: risk.inherent_risk_score,
        },
        controls: linkedControls.map(c => ({
          name: c.name,
          health_score: c.health_score,
          status: c.status,
          type: c.control_type,
        })),
        average_control_health: avgControlHealth,
        risk_reduction: ((risk.inherent_risk_score - risk.residual_risk_score) / risk.inherent_risk_score * 100).toFixed(1),
      };

      const response = await axios.post(`${API}/ai/analyze`, {
        analysis_type: 'control_health_impact',
        context,
      });

      setAiAnalysis({ riskName: risk.name, ...response.data });
      toast.success('Control health impact analyzed');
    } catch (error) {
      console.error('Error analyzing control impact:', error);
      toast.error('Failed to analyze control impact');
    } finally {
      setAnalyzing(false);
    }
  };

  const riskKriKciData = topRisks.map(risk => {
    const linkedKRIs = kris.filter(kri => risk.kris.includes(kri.id));
    const linkedControls = controls.filter(c => risk.linked_controls.includes(c.id));
    const linkedKCIs = kcis.filter(kci => linkedControls.some(c => c.id === kci.control_id));
    
    return {
      name: risk.name.length > 15 ? risk.name.substring(0, 15) + '...' : risk.name,
      riskScore: risk.residual_risk_score,
      kriCount: linkedKRIs.length,
      kciCount: linkedKCIs.length,
      controlHealth: linkedControls.length > 0 
        ? linkedControls.reduce((sum, c) => sum + c.health_score, 0) / linkedControls.length 
        : 0,
    };
  });

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
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-slate-900 mb-2">Risk Intelligence</h1>
          <p className="text-lg text-slate-600">AI-powered Risk-KRI-KCI mapping with dynamic control health impact</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6"
            data-testid="chart-risk-kri-kci"
          >
            <h3 className="text-xl font-semibold text-slate-900 mb-4">Top 10 Risks: KRI-KCI Mapping</h3>
            <ResponsiveContainer width="100%" height={350}>
              <BarChart data={riskKriKciData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
                <XAxis dataKey="name" stroke="#64748b" angle={-45} textAnchor="end" height={100} />
                <YAxis stroke="#64748b" />
                <Tooltip
                  contentStyle={{ backgroundColor: '#fff', border: '1px solid #e2e8f0', borderRadius: '8px' }}
                />
                <Legend />
                <Bar dataKey="riskScore" fill="#ef4444" name="Risk Score" />
                <Bar dataKey="kriCount" fill="#3b82f6" name="KRIs" />
                <Bar dataKey="kciCount" fill="#10b981" name="KCIs" />
              </BarChart>
            </ResponsiveContainer>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6"
            data-testid="chart-control-health-impact"
          >
            <h3 className="text-xl font-semibold text-slate-900 mb-4">Control Health Impact on Risk</h3>
            <ResponsiveContainer width="100%" height={350}>
              <BarChart data={riskKriKciData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
                <XAxis dataKey="name" stroke="#64748b" angle={-45} textAnchor="end" height={100} />
                <YAxis stroke="#64748b" />
                <Tooltip
                  contentStyle={{ backgroundColor: '#fff', border: '1px solid #e2e8f0', borderRadius: '8px' }}
                />
                <Legend />
                <Bar dataKey="controlHealth" fill="#10b981" name="Avg Control Health %" />
                <Bar dataKey="riskScore" fill="#ef4444" name="Risk Score" />
              </BarChart>
            </ResponsiveContainer>
            <p className="text-sm text-slate-600 mt-4">
              Higher control health correlates with lower risk scores - demonstrating dynamic risk mitigation
            </p>
          </motion.div>
        </div>

        <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6 mb-6">
          <h3 className="text-xl font-semibold text-slate-900 mb-4">Top 10 Risks with AI Analysis</h3>
          <div className="space-y-3">
            {topRisks.map((risk, idx) => {
              const linkedKRIs = kris.filter(kri => risk.kris.includes(kri.id));
              const linkedControls = controls.filter(c => risk.linked_controls.includes(c.id));
              const linkedKCIs = kcis.filter(kci => linkedControls.some(c => c.id === kci.control_id));
              const avgControlHealth = linkedControls.length > 0
                ? (linkedControls.reduce((sum, c) => sum + c.health_score, 0) / linkedControls.length).toFixed(0)
                : 0;

              return (
                <div
                  key={risk.id}
                  className="border border-slate-200 rounded-lg p-4 hover:border-blue-300 hover:shadow-md transition-all duration-200"
                  data-testid={`risk-item-${idx}`}
                >
                  <div className="flex items-start justify-between">
                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2">
                        <div className="h-10 w-10 rounded-full bg-red-100 flex items-center justify-center">
                          <span className="text-sm font-bold text-red-600">#{idx + 1}</span>
                        </div>
                        <div>
                          <h4 className="font-semibold text-slate-900">{risk.name}</h4>
                          <p className="text-sm text-slate-600">{risk.description}</p>
                        </div>
                      </div>
                      
                      <div className="grid grid-cols-2 md:grid-cols-5 gap-4 mt-4 mb-3">
                        <div>
                          <p className="text-xs text-slate-500">Risk Score</p>
                          <p className="text-lg font-bold text-red-600">{risk.residual_risk_score.toFixed(1)}</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">KRIs</p>
                          <p className="text-lg font-bold text-blue-600">{linkedKRIs.length}</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">KCIs</p>
                          <p className="text-lg font-bold text-green-600">{linkedKCIs.length}</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">Controls</p>
                          <p className="text-lg font-bold text-slate-900">{linkedControls.length}</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">Control Health</p>
                          <p className="text-lg font-bold text-emerald-600">{avgControlHealth}%</p>
                        </div>
                      </div>

                      {risk.ai_insights && (
                        <div className="bg-blue-50 border border-blue-200 rounded-lg p-3 mb-3">
                          <div className="flex items-start gap-2">
                            <Brain className="h-4 w-4 text-blue-600 mt-0.5" />
                            <div>
                              <p className="text-xs font-semibold text-blue-900 mb-1">AI Insight</p>
                              <p className="text-sm text-blue-800">{risk.ai_insights}</p>
                            </div>
                          </div>
                        </div>
                      )}

                      <div className="flex gap-2">
                        <button
                          onClick={() => analyzeRiskKRIMapping(risk)}
                          disabled={analyzing}
                          data-testid={`analyze-kri-mapping-${idx}`}
                          className="inline-flex items-center gap-2 px-3 py-1.5 bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium rounded-md transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
                        >
                          {analyzing ? <Loader2 className="h-4 w-4 animate-spin" /> : <Brain className="h-4 w-4" />}
                          Analyze KRI-KCI Mapping
                        </button>
                        <button
                          onClick={() => analyzeControlHealthImpact(risk)}
                          disabled={analyzing}
                          data-testid={`analyze-control-health-${idx}`}
                          className="inline-flex items-center gap-2 px-3 py-1.5 bg-green-600 hover:bg-green-700 text-white text-sm font-medium rounded-md transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
                        >
                          {analyzing ? <Loader2 className="h-4 w-4 animate-spin" /> : <Activity className="h-4 w-4" />}
                          Analyze Control Impact
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {aiAnalysis && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-lg border border-blue-200 shadow-lg p-6"
            data-testid="ai-analysis-result"
          >
            <div className="flex items-center gap-3 mb-4">
              <div className="h-12 w-12 rounded-full bg-blue-600 flex items-center justify-center">
                <Brain className="h-6 w-6 text-white" />
              </div>
              <div>
                <h3 className="text-xl font-bold text-slate-900">AI Analysis: {aiAnalysis.riskName}</h3>
                <p className="text-sm text-slate-600">Generated by GPT-4o</p>
              </div>
            </div>

            <div className="bg-white rounded-lg p-4 mb-4">
              <h4 className="font-semibold text-slate-900 mb-2">Analysis</h4>
              <p className="text-slate-700 leading-relaxed">{aiAnalysis.analysis}</p>
            </div>

            {aiAnalysis.recommendations && aiAnalysis.recommendations.length > 0 && (
              <div className="bg-white rounded-lg p-4">
                <h4 className="font-semibold text-slate-900 mb-3">Recommendations</h4>
                <div className="space-y-2">
                  {aiAnalysis.recommendations.map((rec, idx) => (
                    <div key={idx} className="flex items-start gap-2">
                      <ArrowRight className="h-5 w-5 text-blue-600 mt-0.5 flex-shrink-0" />
                      <p className="text-slate-700">{rec}</p>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </motion.div>
        )}
      </motion.div>
    </div>
  );
};

export default RiskIntelligence;
