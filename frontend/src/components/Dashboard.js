import RiskPanel from "./RiskPanel";
import MetricsPanel from "./MetricsPanel";
import ServiceMap from "./ServiceMap";
import IncidentTimeline from "./IncidentTimeline";
import AIInsights from "./AIInsights";

function Dashboard() {
  return (
    <div>
      <h1>AI-Powered Predictive Cloud Observability Platform</h1>

      <div className="grid">
        <RiskPanel />
        <MetricsPanel />
        <ServiceMap />
        <IncidentTimeline />
        <AIInsights />
      </div>
    </div>
  );
}

export default Dashboard;