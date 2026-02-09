import React from 'react';
import { motion } from 'framer-motion';
import { Target, Construction } from 'lucide-react';

const KCIManagement = () => {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
        <div className="mb-8">
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight text-slate-900 mb-2">KCI Management</h1>
          <p className="text-lg text-slate-600">Key Control Indicators linked to KRIs</p>
        </div>
        <div className="bg-white rounded-lg border border-slate-200 shadow-sm p-12 text-center">
          <Construction className="h-16 w-16 text-slate-300 mx-auto mb-4" />
          <h3 className="text-xl font-bold text-slate-900 mb-2">Coming Soon</h3>
          <p className="text-slate-600">KCI creation and performance tracking</p>
        </div>
      </motion.div>
    </div>
  );
};

export default KCIManagement;
