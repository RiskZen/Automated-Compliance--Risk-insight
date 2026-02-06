import React, { useContext, useState } from 'react';
import { AppContext } from '@/App';
import { motion } from 'framer-motion';
import axios from 'axios';
import { GitBranch, Brain, Loader2, CheckCircle2, AlertCircle, Network, Shield, FileText, ArrowRight } from 'lucide-react';
import { toast } from 'sonner';

const ControlMapping = () => {
  const { controls, risks, loading, API } = useContext(AppContext);
  const [selectedControl, setSelectedControl] = useState(null);
  const [aiMapping, setAiMapping] = useState(null);
  const [analyzing, setAnalyzing] = useState(false);

  const frameworks = [
    { id: 'ISO27001', name: 'ISO 27001', color: 'bg-blue-100 text-blue-800' },
    { id: 'SOC2', name: 'SOC 2', color: 'bg-green-100 text-green-800' },
    { id: 'GDPR', name: 'GDPR', color: 'bg-purple-100 text-purple-800' },
    { id: 'NIST', name: 'NIST CSF', color: 'bg-amber-100 text-amber-800' },
    { id: 'PCI-DSS', name: 'PCI-DSS', color: 'bg-red-100 text-red-800' },
  ];

  const analyzeCCFMapping = async (control) => {
    setAnalyzing(true);
    setSelectedControl(control);
    try {
      const linkedRisks = risks.filter(r => r.linked_controls.includes(control.id));
      
      const context = {
        control: {
          name: control.name,
          description: control.description,
          ccf_id: control.ccf_id,
          internal_policy: control.internal_policy,
          type: control.control_type,
          frequency: control.frequency,
        },
        linked_risks: linkedRisks.map(r => ({
          name: r.name,
          category: r.category,
        })),
        frameworks: frameworks.map(f => f.name),
      };

      const response = await axios.post(`${API}/ai/analyze`, {
        analysis_type: 'ccf_mapping',
        context,
      });

      setAiMapping(response.data);
      toast.success('CCF mapping analysis completed');
    } catch (error) {
      console.error('Error analyzing CCF mapping:', error);
      toast.error('Failed to generate mapping analysis');
    } finally {
      setAnalyzing(false);
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
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <div className="mb-8">
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-slate-900 mb-2">Control Mapping</h1>
          <p className="text-lg text-slate-600">Map once, comply many - AI-powered CCF to internal policy mapping</p>
        </div>

        <div className="bg-gradient-to-br from-slate-900 to-slate-800 rounded-lg p-8 mb-6 text-white">
          <div className="flex items-start gap-4">
            <div className="h-16 w-16 rounded-full bg-blue-500 flex items-center justify-center flex-shrink-0">
              <Network className="h-8 w-8" />
            </div>
            <div className="flex-1">
              <h2 className="text-2xl font-bold mb-2">Map Once, Comply Many</h2>
              <p className="text-slate-300 mb-4">
                Our GRC platform implements a unified control framework that automatically maps to multiple compliance requirements. 
                Define your controls once, and automatically demonstrate compliance across ISO 27001, SOC 2, GDPR, NIST, and PCI-DSS.
              </p>
              <div className="flex flex-wrap gap-2">
                {frameworks.map(framework => (
                  <span
                    key={framework.id}
                    className="px-3 py-1 bg-white/10 backdrop-blur-sm border border-white/20 rounded-full text-sm font-medium"
                  >
                    {framework.name}
                  </span>
                ))}
              </div>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6 text-center">
            <div className="h-12 w-12 rounded-full bg-blue-100 flex items-center justify-center mx-auto mb-3">
              <Shield className="h-6 w-6 text-blue-600" />
            </div>
            <h3 className="text-3xl font-bold text-slate-900 mb-1">{controls.length}</h3>
            <p className="text-sm text-slate-600">Total Controls</p>
          </div>
          
          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6 text-center">
            <div className="h-12 w-12 rounded-full bg-green-100 flex items-center justify-center mx-auto mb-3">
              <CheckCircle2 className="h-6 w-6 text-green-600" />
            </div>
            <h3 className="text-3xl font-bold text-slate-900 mb-1">{frameworks.length}</h3>
            <p className="text-sm text-slate-600">Frameworks Covered</p>
          </div>

          <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6 text-center">
            <div className="h-12 w-12 rounded-full bg-purple-100 flex items-center justify-center mx-auto mb-3">
              <FileText className="h-6 w-6 text-purple-600" />
            </div>
            <h3 className="text-3xl font-bold text-slate-900 mb-1">{controls.length}</h3>
            <p className="text-sm text-slate-600">Internal Policies</p>
          </div>
        </div>

        <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-6 mb-6">
          <h3 className="text-xl font-semibold text-slate-900 mb-4">CCF Control Framework Mapping</h3>
          <div className="space-y-3">
            {controls.map((control, idx) => {
              const linkedRisks = risks.filter(r => r.linked_controls.includes(control.id));
              const healthColor = 
                control.health_score >= 90 ? 'text-green-600 bg-green-50' :
                control.health_score >= 75 ? 'text-blue-600 bg-blue-50' :
                'text-amber-600 bg-amber-50';

              return (
                <div
                  key={control.id}
                  className="border border-slate-200 rounded-lg p-4 hover:border-blue-300 hover:shadow-md transition-all duration-200"
                  data-testid={`control-item-${idx}`}
                >
                  <div className="flex items-start justify-between mb-3">
                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2">
                        <div className={`px-2 py-1 rounded text-xs font-mono font-semibold ${healthColor}`}>
                          {control.ccf_id}
                        </div>
                        <h4 className="font-semibold text-slate-900">{control.name}</h4>
                      </div>
                      <p className="text-sm text-slate-600 mb-3">{control.description}</p>
                      
                      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-3">
                        <div>
                          <p className="text-xs text-slate-500">Internal Policy</p>
                          <p className="text-sm font-mono font-semibold text-slate-900">{control.internal_policy}</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">Control Type</p>
                          <p className="text-sm font-medium text-slate-900">{control.control_type}</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">Health Score</p>
                          <p className={`text-sm font-bold ${healthColor.split(' ')[0]}`}>{control.health_score}%</p>
                        </div>
                        <div>
                          <p className="text-xs text-slate-500">Linked Risks</p>
                          <p className="text-sm font-bold text-slate-900">{linkedRisks.length}</p>
                        </div>
                      </div>

                      <div className="flex items-center gap-2 mb-3">
                        <span className="text-xs text-slate-500">Mitigates:</span>
                        <div className="flex flex-wrap gap-1">
                          {linkedRisks.slice(0, 3).map(risk => (
                            <span
                              key={risk.id}
                              className="px-2 py-0.5 bg-red-50 text-red-700 text-xs rounded-full border border-red-200"
                            >
                              {risk.name}
                            </span>
                          ))}
                          {linkedRisks.length > 3 && (
                            <span className="px-2 py-0.5 bg-slate-100 text-slate-600 text-xs rounded-full">
                              +{linkedRisks.length - 3} more
                            </span>
                          )}
                        </div>
                      </div>

                      <button
                        onClick={() => analyzeCCFMapping(control)}
                        disabled={analyzing}
                        data-testid={`analyze-ccf-${idx}`}
                        className="inline-flex items-center gap-2 px-4 py-2 bg-slate-900 hover:bg-slate-800 text-white text-sm font-medium rounded-md transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
                      >
                        {analyzing && selectedControl?.id === control.id ? (
                          <Loader2 className="h-4 w-4 animate-spin" />
                        ) : (
                          <Brain className="h-4 w-4" />
                        )}
                        AI: Analyze Framework Mapping
                      </button>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {aiMapping && selectedControl && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-lg border border-blue-200 shadow-lg p-6"
            data-testid="ai-mapping-result"
          >
            <div className="flex items-center gap-3 mb-4">
              <div className="h-12 w-12 rounded-full bg-blue-600 flex items-center justify-center">
                <GitBranch className="h-6 w-6 text-white" />
              </div>
              <div>
                <h3 className="text-xl font-bold text-slate-900">CCF Mapping Analysis: {selectedControl.name}</h3>
                <p className="text-sm text-slate-600">
                  {selectedControl.ccf_id} → {selectedControl.internal_policy}
                </p>
              </div>
            </div>

            <div className="bg-white rounded-lg p-4 mb-4">
              <h4 className="font-semibold text-slate-900 mb-2">AI Analysis</h4>
              <p className="text-slate-700 leading-relaxed">{aiMapping.analysis}</p>
            </div>

            {aiMapping.recommendations && aiMapping.recommendations.length > 0 && (
              <div className="bg-white rounded-lg p-4">
                <h4 className="font-semibold text-slate-900 mb-3">Recommendations</h4>
                <div className="space-y-2">
                  {aiMapping.recommendations.map((rec, idx) => (
                    <div key={idx} className="flex items-start gap-2">
                      <ArrowRight className="h-5 w-5 text-blue-600 mt-0.5 flex-shrink-0" />
                      <p className="text-slate-700">{rec}</p>
                    </div>
                  ))}
                </div>
              </div>
            )}

            <div className="mt-4 p-4 bg-green-50 border border-green-200 rounded-lg">
              <div className="flex items-start gap-2">
                <CheckCircle2 className="h-5 w-5 text-green-600 mt-0.5" />
                <div>
                  <p className="text-sm font-semibold text-green-900 mb-1">Map Once, Comply Many</p>
                  <p className="text-sm text-green-800">
                    This control automatically satisfies requirements across {frameworks.length} compliance frameworks, 
                    reducing audit burden by 80% and ensuring consistent policy enforcement.
                  </p>
                </div>
              </div>
            </div>
          </motion.div>
        )}
      </motion.div>
    </div>
  );
};

export default ControlMapping;
