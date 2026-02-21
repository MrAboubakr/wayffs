<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero__content animate-fade-in">
        <span class="hero__badge">🚀 Project Management Reimagined</span>
        <h1 class="hero__title">
          Track, Collaborate &
          <span class="text-gradient-brand">Ship Faster</span>
        </h1>
        <p class="hero__subtitle">
          Wayffs empowers teams to manage projects with real-time tracking, seamless collaboration, and beautiful dashboards — all in one place.
        </p>
        <div class="hero__actions">
          <router-link to="/register" class="btn-wayfs btn-primary btn-lg">
            Get Started Free
          </router-link>
          <router-link to="/login" class="btn-wayfs btn-outline btn-lg">
            Sign In →
          </router-link>
        </div>
      </div>
    </section>

    <!-- Full-Width Visual Rectangle -->
    <section class="hero__showcase animate-fade-in-delay-2">
      <div class="hero__showcase-inner">
        <!-- Left: Task Animation -->
        <div class="hero__task-card-large card-wayfs">
          <div class="task-vertical-sequence">
            <div class="task-vertical-highlight" :style="{ transform: `translateY(${activeHeroStep * 50}px)`, opacity: activeHeroStep >= 0 ? 1 : 0 }"></div>
            
            <div v-for="(task, i) in heroTasks" :key="i" class="hero-task-row" :class="{ 'checked': activeHeroStep >= i, 'active': activeHeroStep === i }">
              <div class="row-check-wrapper">
                <span class="row-check">✓</span>
              </div>
              <span class="row-text">{{ task }}</span>
            </div>
          </div>
          <div class="task-bar-bottom">
            <div class="task-bar-fill" :style="{ width: (activeHeroStep + 1) * 25 + '%' }"></div>
          </div>
        </div>

        <!-- Right: Floating Stats Cards -->
        <div class="hero__visual">
          <div class="hero__card hero__card--1">
            <div class="hero__card-icon">📊</div>
            <span>3 Active Projects</span>
          </div>
          <div class="hero__card hero__card--2">
            <div class="hero__card-icon">✅</div>
            <span>12 Tasks Completed</span>
          </div>
          <div class="hero__card hero__card--3">
            <div class="hero__card-icon">👥</div>
            <span>5 Team Members</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="features">
      <div class="features__header animate-fade-in">
        <h2 class="section-title text-gradient-brand">Why Wayffs?</h2>
        <p class="section-subtitle">Everything you need to manage projects like a pro</p>
      </div>
      <div class="features__grid">
        <div class="feature-card animate-fade-in-delay-1" v-for="(feature, index) in features" :key="index">
          <div class="feature-card__icon" :style="{ background: feature.bg }">
            {{ feature.icon }}
          </div>
          <h3 class="feature-card__title">{{ feature.title }}</h3>
          <p class="feature-card__desc">{{ feature.desc }}</p>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta animate-fade-in">
      <div class="cta__content">
        <h2 class="cta__title">Ready to ship faster?</h2>
        <p class="cta__desc">Join thousands of teams already using Wayffs to track and deliver projects.</p>
        <router-link to="/register" class="btn-wayfs btn-secondary btn-lg">
          Start Your Free Account
        </router-link>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

const heroTasks = ['Create Project', 'Add Team Members', 'Set Milestones', 'Deliver Faster'];
const activeHeroStep = ref(-1);

onMounted(() => {
  setInterval(() => {
    if (activeHeroStep.value >= 3) {
      activeHeroStep.value = -1;
    } else {
      activeHeroStep.value++;
    }
  }, 1500);
});

const features = [
  {
    icon: '🔗',
    title: 'Track ID Sharing',
    desc: 'Share a unique Track ID with collaborators so they can follow your project progress in real time.',
    bg: 'linear-gradient(135deg, #0A7B3B, #10B860)',
  },
  {
    icon: '📊',
    title: 'Visual Dashboards',
    desc: 'See all your projects, tasks, and metrics at a glance with a clean, modern dashboard.',
    bg: 'linear-gradient(135deg, #0D9647, #10B860)',
  },
  {
    icon: '✅',
    title: 'Task Management',
    desc: 'Create, assign, and track tasks with status badges and real-time updates.',
    bg: 'linear-gradient(135deg, #0D9647, #22C55E)',
  },
  {
    icon: '🌙',
    title: 'Dark Mode',
    desc: 'A beautiful dark theme with animated gradients for comfortable late-night work sessions.',
    bg: 'linear-gradient(135deg, #F5B800, #10B860)',
  },
  {
    icon: '📱',
    title: 'Fully Responsive',
    desc: 'Works beautifully on desktop, tablet, and mobile so you can manage on the go.',
    bg: 'linear-gradient(135deg, #C13A2A, #E04B1A)',
  },
  {
    icon: '🔒',
    title: 'Secure & Private',
    desc: 'Role-based access ensures your data stays secure and only visible to the right people.',
    bg: 'linear-gradient(135deg, #0A7B3B, #0D9647)',
  },
];
</script>

<style scoped>
.home {
  width: 100%;
}

/* Hero */
.hero {
  max-width: 1200px;
  margin: 0 auto;
  padding: 5rem 1.5rem 2rem;
  text-align: center;
}

/* Full-Width Showcase Rectangle */
.hero__showcase {
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 1.5rem 4rem;
}

.hero__showcase-inner {
  display: grid;
  grid-template-columns: 1fr 1.4fr;
  gap: 3rem;
  align-items: center;
  background: var(--wayfs-card);
  border: 1px solid var(--wayfs-border);
  border-radius: 2rem;
  padding: 3rem;
  position: relative;
  overflow: hidden;
  backdrop-filter: blur(16px);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
}

.hero__badge {
  display: inline-block;
  padding: 0.4rem 1rem;
  border-radius: 9999px;
  font-size: 0.8rem;
  font-weight: 600;
  background: rgba(13, 150, 71, 0.1);
  color: #0D9647;
  border: 1px solid rgba(13, 150, 71, 0.2);
  margin-bottom: 1.5rem;
}

:global(.dark) .hero__badge {
  background: rgba(245, 184, 0, 0.1);
  color: #10B860;
  border-color: rgba(245, 184, 0, 0.2);
}

.hero__title {
  font-size: 3.25rem;
  font-weight: 900;
  line-height: 1.1;
  color: var(--wayfs-text);
  margin-bottom: 1.25rem;
}

.hero__subtitle {
  font-size: 1.1rem;
  color: var(--wayfs-text-secondary);
  line-height: 1.6;
  max-width: 500px;
  margin-bottom: 2rem;
}

.hero__actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
}

.btn-lg {
  padding: 0.8rem 2rem;
  font-size: 1rem;
}

/* Hero floating cards */
.hero__visual {
  position: relative;
  height: 320px;
}

.hero__card {
  position: absolute;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 1.25rem;
  background: var(--wayfs-card);
  border: 1px solid var(--wayfs-border);
  border-radius: 0.75rem;
  backdrop-filter: blur(12px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--wayfs-text);
  animation: float 6s ease-in-out infinite;
}

.hero__card-icon {
  font-size: 1.5rem;
}

.hero__card--1 {
  top: 10%;
  right: 10%;
  animation-delay: 0s;
}

.hero__card--2 {
  top: 45%;
  left: 5%;
  animation-delay: 2s;
}

.hero__card--3 {
  bottom: 5%;
  right: 15%;
  animation-delay: 4s;
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-12px); }
}

/* Features */
.features {
  max-width: 1200px;
  margin: 0 auto;
  padding: 4rem 1.5rem;
}

.features__header {
  text-align: center;
  margin-bottom: 3rem;
}

.features__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.feature-card {
  background: var(--wayfs-card);
  border: 1px solid var(--wayfs-border);
  border-radius: 1rem;
  padding: 1.75rem;
  backdrop-filter: blur(12px);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 48px rgba(13, 150, 71, 0.12);
}

:global(.dark) .feature-card:hover {
  box-shadow: 0 16px 48px rgba(245, 184, 0, 0.12);
}

.feature-card__icon {
  width: 48px;
  height: 48px;
  border-radius: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  margin-bottom: 1rem;
}

.feature-card__title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--wayfs-text);
  margin-bottom: 0.5rem;
}

.feature-card__desc {
  font-size: 0.85rem;
  color: var(--wayfs-text-secondary);
  line-height: 1.5;
}

/* CTA */
.cta {
  max-width: 1200px;
  margin: 0 auto;
  padding: 4rem 1.5rem 5rem;
}

.cta__content {
  text-align: center;
  background: linear-gradient(135deg, rgba(13, 150, 71, 0.08), rgba(245, 184, 0, 0.08));
  border: 1px solid var(--wayfs-border);
  border-radius: 1.5rem;
  padding: 4rem 2rem;
}

:global(.dark) .cta__content {
  background: linear-gradient(135deg, rgba(13, 150, 71, 0.15), rgba(245, 184, 0, 0.1));
}

.cta__title {
  font-size: 2rem;
  font-weight: 800;
  color: var(--wayfs-text);
  margin-bottom: 0.75rem;
}

.cta__desc {
  font-size: 1rem;
  color: var(--wayfs-text-secondary);
  margin-bottom: 2rem;
  max-width: 480px;
  margin-left: auto;
  margin-right: auto;
}

/* Large Vertical Task Card Styles */
.hero__task-card-large {
  margin-top: 3.5rem;
  width: 100%;
  max-width: 600px;
  background: var(--wayfs-card);
  border: 1px solid var(--wayfs-border);
  border-radius: 1.5rem;
  padding: 2.5rem;
  backdrop-filter: blur(20px);
  position: relative;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
}

.task-vertical-sequence {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 0;
  margin-bottom: 2.5rem;
}

.task-vertical-highlight {
  position: absolute;
  top: -0.5rem;
  left: -1rem;
  right: -1rem;
  height: 60px;
  background: linear-gradient(90deg, rgba(13, 150, 71, 0.15), transparent);
  border-left: 4px solid #10B860;
  border-radius: 8px;
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  pointer-events: none;
  z-index: 0;
}

.hero-task-row {
  position: relative;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  height: 60px;
  padding: 0 1.5rem;
  opacity: 0.2;
  transition: all 0.5s ease;
  z-index: 1;
}

.hero-task-row.active {
  opacity: 1;
  font-weight: 800;
  transform: translateX(10px);
}

.hero-task-row.checked:not(.active) {
  opacity: 0.7;
}

.row-check-wrapper {
  flex-shrink: 0;
}

.row-check {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 2px solid var(--wayfs-border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.9rem;
  font-weight: 900;
  color: transparent;
  transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
  background: var(--wayfs-surface);
}

.checked .row-check {
  background: linear-gradient(135deg, #0D9647, #10B860);
  border-color: transparent;
  color: #fff;
  transform: scale(1.1);
  box-shadow: 0 0 15px rgba(16, 184, 96, 0.4);
}

.row-text {
  font-size: 1.2rem;
  color: var(--wayfs-text);
  transition: all 0.3s ease;
}

.checked .row-text {
  color: var(--wayfs-text);
}

.task-bar-bottom {
  height: 6px;
  background: var(--wayfs-border);
  border-radius: 999px;
  overflow: hidden;
  margin: 0;
}

.task-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #F5B800, #A8D400, #10B860);
  transition: width 0.8s ease;
}

/* Responsive */
@media (max-width: 768px) {
  .hero {
    padding: 3rem 1.5rem 1rem;
  }

  .hero__title {
    font-size: 2.25rem;
  }

  .hero__subtitle {
    margin-left: auto;
    margin-right: auto;
  }

  .hero__showcase-inner {
    grid-template-columns: 1fr;
    padding: 1.5rem;
    gap: 2rem;
  }

  .hero__task-card-large {
    max-width: 100%;
    padding: 1.5rem;
  }

  .hero__visual {
    display: none;
  }

  .features__grid {
    grid-template-columns: 1fr;
  }
}

@media (min-width: 769px) and (max-width: 1024px) {
  .features__grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
