import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { LayoutDashboard, ShieldAlert, GitBranch, FileCheck, Sparkles } from 'lucide-react';

const Sidebar = () => {
  const location = useLocation();

  const menuItems = [
    { path: '/', icon: LayoutDashboard, label: 'Dashboard', testId: 'nav-dashboard' },
    { path: '/risk-intelligence', icon: ShieldAlert, label: 'Risk Intelligence', testId: 'nav-risk' },
    { path: '/control-mapping', icon: GitBranch, label: 'Control Mapping', testId: 'nav-controls' },
    { path: '/evidence', icon: FileCheck, label: 'Evidence Collection', testId: 'nav-evidence' },
  ];

  return (
    <>
      <aside className="fixed left-0 top-0 z-40 h-screen w-64 bg-slate-900 text-slate-300 transition-transform -translate-x-full md:translate-x-0">
        <div className="h-full px-3 py-6 overflow-y-auto">
          <div className="mb-8 px-3">
            <div className="flex items-center gap-2">
              <Sparkles className="h-7 w-7 text-blue-400" />
              <div>
                <h1 className="text-xl font-bold text-white">GRC Intelligence</h1>
                <p className="text-xs text-slate-400">Strategic Command Center</p>
              </div>
            </div>
          </div>

          <nav className="space-y-2">
            {menuItems.map((item) => {
              const Icon = item.icon;
              const isActive = location.pathname === item.path;
              return (
                <Link
                  key={item.path}
                  to={item.path}
                  data-testid={item.testId}
                  className={`flex items-center gap-3 px-3 py-2.5 rounded-md transition-all duration-200 ${
                    isActive
                      ? 'bg-slate-800 text-white shadow-sm'
                      : 'text-slate-300 hover:bg-slate-800 hover:text-white'
                  }`}
                >
                  <Icon className="h-5 w-5" />
                  <span className="font-medium">{item.label}</span>
                </Link>
              );
            })}
          </nav>

          <div className="mt-auto pt-8 px-3">
            <div className="p-4 rounded-lg bg-slate-800 border border-slate-700">
              <p className="text-xs text-slate-400 mb-2">AI-Powered GRC</p>
              <p className="text-sm text-slate-200 font-medium">Transform compliance into strategic advantage</p>
            </div>
          </div>
        </div>
      </aside>
    </>
  );
};

export default Sidebar;
