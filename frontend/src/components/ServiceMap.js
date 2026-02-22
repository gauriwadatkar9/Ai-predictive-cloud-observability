function ServiceMap() {
  return (
    <div className="card">
      <h2>Service Dependency Visualization</h2>
      <p>API Service → Auth Service → Database</p>
      <p>Business Impact: Revenue-critical service degradation detected.</p>
    </div>
  );
}

export default ServiceMap;