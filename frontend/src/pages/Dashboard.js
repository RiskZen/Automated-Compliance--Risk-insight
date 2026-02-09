import React, { useContext, useEffect, useState } from 'react';
import { AppContext } from '@/App';
import { motion } from 'framer-motion';
import axios from 'axios';
import { Shield, CheckCircle2, AlertTriangle, TrendingDown, Activity, BarChart3 } from 'lucide-react';
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';

const Dashboard = () => {
  const { frameworks, unifiedControls, controlTests, issues, risks, loading, API } = useContext(AppContext);
  const [stats, setStats] = useState(null);

  useEffect(() => {
    fetchDashboardStats();
  }, [controlTests, issues]);

  const fetchDashboardStats = async () => {
    try {
      const response = await axios.get(`${API}/dashboard/stats`);
      setStats(response.data);
    } catch (error) {
      console.error('Error fetching dashboard stats:', error);
    }
  };

  const enabledFrameworks = frameworks.filter(f => f.enabled);
  const openIssues = issues.filter(i => !['Resolved', 'Closed'].includes(i.status));
  
  const issuesBySeverity = issues.reduce((acc, issue) => {
    const existing = acc.find(item => item.name === issue.severity);
    if (existing) {
      existing.value += 1;
    } else {
      acc.push({ name: issue.severity, value: 1 });
    }
    return acc;
  }, []);

  const COLORS = ['#ef4444', '#f59e0b', '#3b82f6', '#10b981'];

  if (loading || !stats) {
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
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-slate-900 mb-2">GRC Dashboard</h1>
          <p className="text-lg text-slate-600">Real-time compliance and risk management overview</p>
        </div>

        {/* Key Metrics */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-6">
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.1 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6 hover:shadow-md transition-shadow duration-200"
            data-testid="metric-frameworks"
          >
            <div className="flex items-center justify-between mb-4">
              <div className="h-10 w-10 rounded-full bg-blue-50 flex items-center justify-center">
                <Shield className="h-5 w-5 text-blue-600" />
              </div>
            </div>
            <p className="text-sm text-slate-500 mb-1">Enabled Frameworks</p>
            <p className="text-3xl font-bold text-slate-900">{stats.enabled_frameworks}</p>
            <p className="text-xs text-slate-600 mt-2">{unifiedControls.length} unified controls</p>
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
              {stats.control_effectiveness > 80 && <TrendingDown className="h-5 w-5 text-green-600" />}
            </div>
            <p className="text-sm text-slate-500 mb-1">Control Effectiveness</p>
            <p className="text-3xl font-bold text-slate-900">{stats.control_effectiveness}%</p>
            <p className="text-xs text-green-600 mt-2">{stats.passed_tests} of {stats.total_tests_performed} passed</p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.3 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6 hover:shadow-md transition-shadow duration-200"
            data-testid="metric-open-issues"
          >
            <div className="flex items-center justify-between mb-4">
              <div className="h-10 w-10 rounded-full bg-red-50 flex items-center justify-center">
                <AlertTriangle className="h-5 w-5 text-red-600" />
              </div>
            </div>
            <p className="text-sm text-slate-500 mb-1">Open Issues</p>
            <p className="text-3xl font-bold text-slate-900">{stats.open_issues}</p>
            <p className="text-xs text-slate-600 mt-2">{stats.total_issues} total issues</p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.4 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6 hover:shadow-md transition-shadow duration-200"
            data-testid="metric-risks"
          >
            <div className="flex items-center justify-between mb-4">
              <div className="h-10 w-10 rounded-full bg-amber-50 flex items-center justify-center">
                <BarChart3 className="h-5 w-5 text-amber-600" />
              </div>
            </div>
            <p className="text-sm text-slate-500 mb-1">Average Risk Score</p>
            <p className="text-3xl font-bold text-slate-900">{stats.avg_residual_risk.toFixed(1)}</p>
            <p className="text-xs text-slate-600 mt-2">{stats.total_risks} risks tracked</p>
          </motion.div>
        </div>

        {/* Charts Row */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6"
            data-testid="chart-frameworks"
          >
            <h3 className="text-xl font-semibold text-slate-900 mb-4">Enabled Frameworks</h3>
            {enabledFrameworks.length > 0 ? (
              <div className="space-y-3">
                {enabledFrameworks.map((fw) => (
                  <div key={fw.id} className="flex items-center justify-between p-3 bg-slate-50 rounded-lg">
                    <div>
                      <p className="font-medium text-slate-900">{fw.name}</p>
                      <p className="text-sm text-slate-600">{fw.total_controls} controls</p>
                    </div>
                    <div className="px-3 py-1 bg-green-100 text-green-800 rounded-full text-xs font-semibold">
                      Active
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <div className="text-center py-8">
                <Shield className="h-12 w-12 text-slate-300 mx-auto mb-3" />
                <p className="text-slate-600">No frameworks enabled</p>
                <p className="text-sm text-slate-500 mt-1">Enable frameworks to start mapping</p>
              </div>
            )}
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.6 }}
            className="bg-white rounded-lg border border-slate-200 shadow-sm p-6"
            data-testid="chart-issues"
          >
            <h3 className="text-xl font-semibold text-slate-900 mb-4">Issues by Severity</h3>
            {issuesBySeverity.length > 0 ? (
              <ResponsiveContainer width="100%" height={250}>
                <PieChart>
                  <Pie
                    data={issuesBySeverity}
                    cx="50%"
                    cy="50%"
                    labelLine={false}
                    label={(entry) => `${entry.name}: ${entry.value}`}
                    outerRadius={80}
                    fill="#8884d8"
                    dataKey="value"
                  >
                    {issuesBySeverity.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
            ) : (
              <div className="text-center py-8">
                <CheckCircle2 className="h-12 w-12 text-green-400 mx-auto mb-3" />
                <p className="text-slate-600">No issues</p>
                <p className="text-sm text-slate-500 mt-1">All controls passing</p>
              </div>
            )}
          </motion.div>
        </div>

        {/* Recent Issues */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.7 }}
          className="bg-white rounded-lg border border-slate-200 shadow-sm p-6"
          data-testid="section-recent-issues"
        >
          <h3 className="text-xl font-semibold text-slate-900 mb-4">Recent Open Issues</h3>
          {openIssues.length > 0 ? (
            <div className="space-y-3">
              {openIssues.slice(0, 5).map((issue) => (
                <div key={issue.id} className="flex items-start justify-between p-4 border border-slate-200 rounded-lg hover:border-blue-300 transition-colors">
                  <div className="flex-1">
                    <div className="flex items-center gap-2 mb-1">
                      <h4 className="font-medium text-slate-900">{issue.title}</h4>
                      <span className={`px-2 py-0.5 rounded-full text-xs font-semibold ${
                        issue.severity === 'Critical' ? 'bg-red-100 text-red-800' :
                        issue.severity === 'High' ? 'bg-orange-100 text-orange-800' :
                        issue.severity === 'Medium' ? 'bg-yellow-100 text-yellow-800' :
                        'bg-blue-100 text-blue-800'
                      }`}>
                        {issue.severity}
                      </span>
                    </div>
                    <p className="text-sm text-slate-600">{issue.description}</p>
                    <div className="flex items-center gap-4 mt-2 text-xs text-slate-500">
                      <span>Assigned to: {issue.assigned_to}</span>
                      <span>Status: {issue.status}</span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="text-center py-8">
              <CheckCircle2 className="h-12 w-12 text-green-400 mx-auto mb-3" />
              <p className="text-slate-600">No open issues</p>
            </div>
          )}
        </motion.div>
      </motion.div>
    </div>
  );
};

export default Dashboard;
