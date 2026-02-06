import React, { useContext, useState } from 'react';
import { AppContext } from '@/App';
import { motion } from 'framer-motion';
import { TrendingUp, TrendingDown, Activity, Shield, AlertTriangle, CheckCircle2, BarChart3, Zap } from 'lucide-react';
import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';

const Dashboard = () => {
  const { risks, controls, kris, kcis, loading } = useContext(AppContext);

  const avgRiskScore = risks.length > 0
    ? (risks.reduce((sum, r) => sum + r.residual_risk_score, 0) / risks.length).toFixed(1)
    : 0;

  const effectiveControls = controls.filter(c => c.status === 'Effective').length;
  const controlEffectiveness = controls.length > 0
    ? ((effectiveControls / controls.length) * 100).toFixed(0)
    : 0;

  const normalKRIs = kris.filter(k => k.status === 'Normal').length;
  const kriHealth = kris.length > 0
    ? ((normalKRIs / kris.length) * 100).toFixed(0)
    : 0;

  const onTrackKCIs = kcis.filter(k => k.status === 'On Track' || k.status === 'Excellent').length;
  const kciHealth = kcis.length > 0
    ? ((onTrackKCIs / kcis.length) * 100).toFixed(0)
    : 0;

  const riskTrendData = [
    { month: 'Jul', score: 5.2 },
    { month: 'Aug', score: 4.8 },
    { month: 'Sep', score: 4.5 },
    { month: 'Oct', score: 4.2 },
    { month: 'Nov', score: 3.9 },
    { month: 'Dec', score: 3.8 },
    { month: 'Jan', score: 3.7 },
  ];

  const riskByCategory = risks.reduce((acc, risk) => {
    const existing = acc.find(item => item.name === risk.category);
    if (existing) {
      existing.value += 1;
    } else {
      acc.push({ name: risk.category, value: 1 });
    }
    return acc;
  }, []);

  const COLORS = ['#0f172a', '#3b82f6', '#ef4444', '#f59e0b', '#10b981', '#8b5cf6'];

  const topRisks = [...risks]
    .sort((a, b) => b.residual_risk_score - a.residual_risk_score)
    .slice(0, 5);

  const recentActivity = [
    { action: 'Control Health Updated', item: 'MFA Implementation', time: '5 mins ago', type: 'success' },
    { action: 'Risk Score Recalculated', item: 'Data Breach', time: '23 mins ago', type: 'info' },
    { action: 'KRI Threshold Exceeded', item: 'Vendor Security Score', time: '1 hour ago', type: 'warning' },
    { action: 'Evidence Collected', item: 'DR Test Results', time: '3 hours ago', type: 'success' },
  ];

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <div className="text-center">
          <Activity className="h-12 w-12 text-blue-500 animate-spin mx-auto mb-4" />
          <p className="text-slate-600">Loading GRC Intelligence...</p>
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
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-slate-900 mb-2">GRC Command Center</h1>
          <p className="text-lg text-slate-600">Real-time intelligence for strategic risk management</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-6">
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.1 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6 hover:shadow-md transition-shadow duration-200"
            data-testid="metric-risk-score"
          >
            <div className="flex items-center justify-between mb-4">
              <div className="h-10 w-10 rounded-full bg-blue-50 flex items-center justify-center">
                <Shield className="h-5 w-5 text-blue-600" />
              </div>
              <TrendingDown className="h-5 w-5 text-green-600" />
            </div>
            <p className="text-sm text-slate-500 mb-1">Avg Risk Score</p>
            <p className="text-3xl font-bold text-slate-900">{avgRiskScore}</p>
            <p className="text-xs text-green-600 mt-2">↓ 12% from last month</p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.2 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6 hover:shadow-md transition-shadow duration-200"
            data-testid="metric-control-effectiveness"
          >
            <div className="flex items-center justify-between mb-4">
              <div className="h-10 w-10 rounded-full bg-green-50 flex items-center justify-center">
                <CheckCircle2 className="h-5 w-5 text-green-600" />
              </div>
              <TrendingUp className="h-5 w-5 text-green-600" />
            </div>
            <p className="text-sm text-slate-500 mb-1">Control Effectiveness</p>
            <p className="text-3xl font-bold text-slate-900">{controlEffectiveness}%</p>
            <p className="text-xs text-green-600 mt-2">↑ 5% improvement</p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.3 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6 hover:shadow-md transition-shadow duration-200"
            data-testid="metric-kri-health"
          >
            <div className="flex items-center justify-between mb-4">
              <div className="h-10 w-10 rounded-full bg-amber-50 flex items-center justify-center">
                <BarChart3 className="h-5 w-5 text-amber-600" />
              </div>
              <Activity className="h-5 w-5 text-blue-600" />
            </div>
            <p className="text-sm text-slate-500 mb-1">KRI Health</p>
            <p className="text-3xl font-bold text-slate-900">{kriHealth}%</p>
            <p className="text-xs text-slate-600 mt-2">{normalKRIs} of {kris.length} normal</p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.4 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6 hover:shadow-md transition-shadow duration-200"
            data-testid="metric-kci-performance"
          >
            <div className="flex items-center justify-between mb-4">
              <div className="h-10 w-10 rounded-full bg-purple-50 flex items-center justify-center">
                <Zap className="h-5 w-5 text-purple-600" />
              </div>
              <TrendingUp className="h-5 w-5 text-green-600" />
            </div>
            <p className="text-sm text-slate-500 mb-1">KCI Performance</p>
            <p className="text-3xl font-bold text-slate-900">{kciHealth}%</p>
            <p className="text-xs text-green-600 mt-2">{onTrackKCIs} on track</p>
          </motion.div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5 }}
            className="md:col-span-2 bg-white rounded-lg border border-slate-200 shadow-sm p-6"
            data-testid="chart-risk-trend"
          >
            <h3 className="text-xl font-semibold text-slate-900 mb-4">Risk Score Trend</h3>
            <ResponsiveContainer width="100%" height={250}>
              <LineChart data={riskTrendData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
                <XAxis dataKey="month" stroke="#64748b" />
                <YAxis stroke="#64748b" />
                <Tooltip
                  contentStyle={{ backgroundColor: '#fff', border: '1px solid #e2e8f0', borderRadius: '8px' }}
                />
                <Line type="monotone" dataKey="score" stroke="#3b82f6" strokeWidth={3} dot={{ fill: '#3b82f6', r: 5 }} />
              </LineChart>
            </ResponsiveContainer>
            <p className="text-sm text-slate-600 mt-2">Residual risk score trending downward - indicating effective control implementation</p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.6 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6"
            data-testid="chart-risk-distribution"
          >
            <h3 className="text-xl font-semibold text-slate-900 mb-4">Risk Distribution</h3>
            <ResponsiveContainer width="100%" height={250}>
              <PieChart>
                <Pie
                  data={riskByCategory}
                  cx="50%"
                  cy="50%"
                  labelLine={false}
                  label={(entry) => entry.name}
                  outerRadius={80}
                  fill="#8884d8"
                  dataKey="value"
                >
                  {riskByCategory.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </motion.div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.7 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6"
            data-testid="section-top-risks"
          >
            <h3 className="text-xl font-semibold text-slate-900 mb-4">Top Risks</h3>
            <div className="space-y-3">
              {topRisks.map((risk, idx) => (
                <div key={risk.id} className="flex items-center justify-between p-3 bg-slate-50 rounded-lg hover:bg-slate-100 transition-colors duration-200">
                  <div className="flex items-center gap-3">
                    <div className="h-8 w-8 rounded-full bg-red-100 flex items-center justify-center">
                      <span className="text-sm font-bold text-red-600">#{idx + 1}</span>
                    </div>
                    <div>
                      <p className="font-medium text-slate-900">{risk.name}</p>
                      <p className="text-xs text-slate-500">{risk.category}</p>
                    </div>
                  </div>
                  <div className="text-right">
                    <p className="text-lg font-bold text-slate-900">{risk.residual_risk_score.toFixed(1)}</p>
                    <p className="text-xs text-slate-500">Score</p>
                  </div>
                </div>
              ))}
            </div>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.8 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6"
            data-testid="section-recent-activity"
          >
            <h3 className="text-xl font-semibold text-slate-900 mb-4">Recent Activity</h3>
            <div className="space-y-3">
              {recentActivity.map((activity, idx) => (
                <div key={idx} className="flex items-start gap-3 p-3 bg-slate-50 rounded-lg">
                  <div className={`h-8 w-8 rounded-full flex items-center justify-center ${
                    activity.type === 'success' ? 'bg-green-100' :
                    activity.type === 'warning' ? 'bg-amber-100' : 'bg-blue-100'
                  }`}>
                    {activity.type === 'success' && <CheckCircle2 className="h-4 w-4 text-green-600" />}
                    {activity.type === 'warning' && <AlertTriangle className="h-4 w-4 text-amber-600" />}
                    {activity.type === 'info' && <Activity className="h-4 w-4 text-blue-600" />}
                  </div>
                  <div className="flex-1">
                    <p className="text-sm font-medium text-slate-900">{activity.action}</p>
                    <p className="text-xs text-slate-600">{activity.item}</p>
                    <p className="text-xs text-slate-400 mt-1">{activity.time}</p>
                  </div>
                </div>
              ))}
            </div>
          </motion.div>
        </div>
      </motion.div>
    </div>
  );
};

export default Dashboard;
