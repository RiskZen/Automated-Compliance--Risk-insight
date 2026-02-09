import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { LayoutDashboard, Shield, GitBranch, FileText, ClipboardCheck, AlertTriangle, TrendingUp, BarChart3, Target, Sparkles } from 'lucide-react';

const Sidebar = () => {
  const location = useLocation();

  const menuSections = [
    {
      title: 'Overview',
      items: [
        { path: '/', icon: LayoutDashboard, label: 'Dashboard', testId: 'nav-dashboard' },
      ]
    },
    {
      title: 'Framework & Controls',
      items: [
        { path: '/frameworks', icon: Shield, label: 'Frameworks', testId: 'nav-frameworks' },
        { path: '/control-mapping', icon: GitBranch, label: 'Control Mapping', testId: 'nav-mapping' },
        { path: '/policies', icon: FileText, label: 'Policies', testId: 'nav-policies' },
      ]
    },
    {
      title: 'Testing & Issues',
      items: [
        { path: '/control-testing', icon: ClipboardCheck, label: 'Control Testing', testId: 'nav-testing' },
        { path: '/issues', icon: AlertTriangle, label: 'Issue Management', testId: 'nav-issues' },
      ]
    },
    {
      title: 'Risk Management',
      items: [
        { path: '/risks', icon: TrendingUp, label: 'Risks', testId: 'nav-risks' },
        { path: '/kris', icon: BarChart3, label: 'KRIs', testId: 'nav-kris' },
        { path: '/kcis', icon: Target, label: 'KCIs', testId: 'nav-kcis' },
      ]
    },
  ];

  return (
    <aside className="fixed left-0 top-0 z-40 h-screen w-64 bg-slate-900 text-slate-300 transition-transform -translate-x-full md:translate-x-0 overflow-y-auto">
      <div className="h-full px-3 py-6">
        <div className="mb-8 px-3">
          <div className="flex items-center gap-2">
            <Sparkles className="h-7 w-7 text-blue-400" />
            <div>
              <h1 className="text-xl font-bold text-white">GRC Platform</h1>
              <p className="text-xs text-slate-400">Enterprise Edition</p>
            </div>
          </div>
        </div>

        {menuSections.map((section, idx) => (
          <div key={idx} className="mb-6">
            <p className="px-3 mb-2 text-xs font-semibold text-slate-500 uppercase tracking-wider">
              {section.title}
            </p>
            <nav className="space-y-1">
              {section.items.map((item) => {
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
                    <span className="font-medium text-sm">{item.label}</span>
                  </Link>
                );
              })}
            </nav>
          </div>
        ))}

        <div className="mt-auto pt-8 px-3">
          <div className="p-4 rounded-lg bg-slate-800 border border-slate-700">
            <p className="text-xs text-slate-400 mb-2">Production Ready</p>
            <p className="text-sm text-slate-200 font-medium">Complete GRC automation platform</p>
          </div>
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;
