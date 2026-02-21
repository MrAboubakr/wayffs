<template>
  <div class="page-container">
    <div class="page-header animate-fade-in">
      <h1 class="section-title">📈 Analytics</h1>
      <p class="section-subtitle">Deep dive into your project performance and team productivity</p>
    </div>

    <div class="analytics-grid">
      <div class="card-wayfs stats-card animate-fade-in-delay-1">
        <h3 class="card-label">Total Completion Rate</h3>
        <div class="huge-number text-gradient-brand">87%</div>
        <p class="trend positive">↑ 12% from last month</p>
      </div>

      <div class="card-wayfs stats-card animate-fade-in-delay-2">
        <h3 class="card-label">Active Projects</h3>
        <div class="huge-number text-gradient-lime">14</div>
        <p class="trend">Stable this week</p>
      </div>

      <div class="card-wayfs chart-container animate-fade-in-delay-3">
        <h3 class="chart-title">Tasks Finished per Day</h3>
        <div class="mock-chart">
          <!-- Placeholder for a chart -->
          <div v-for="h in [40, 60, 30, 80, 50, 90, 70]" :key="h" class="bar" :style="{ height: h + '%' }"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.analytics-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.stats-card {
  text-align: center;
  padding: 2rem;
}

.card-label {
  font-size: 0.9rem;
  color: var(--wayfs-text-secondary);
  margin-bottom: 0.5rem;
}

.huge-number {
  font-size: 3rem;
  font-weight: 800;
}

.trend {
  font-size: 0.85rem;
  margin-top: 0.5rem;
}

.trend.positive {
  color: #10B860;
}

.chart-container {
  grid-column: span 2;
  padding: 2rem;
}

.chart-title {
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 2rem;
}

.mock-chart {
  height: 200px;
  display: flex;
  align-items: flex-end;
  gap: 1.5rem;
  padding: 0 1rem;
}

.bar {
  flex: 1;
  background: linear-gradient(to top, #0D9647, #10B860);
  border-radius: 4px 4px 0 0;
  min-width: 20px;
  transition: height 1s ease-out;
}

@media (max-width: 768px) {
  .analytics-grid {
    grid-template-columns: 1fr;
  }
  .chart-container {
    grid-column: span 1;
  }
}
</style>
