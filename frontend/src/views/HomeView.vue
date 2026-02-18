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
      <div class="hero__visual animate-fade-in-delay-2">
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
const features = [
  {
    icon: '🔗',
    title: 'Track ID Sharing',
    desc: 'Share a unique Track ID with collaborators so they can follow your project progress in real time.',
    bg: 'linear-gradient(135deg, #316D70, #48C6CB)',
  },
  {
    icon: '📊',
    title: 'Visual Dashboards',
    desc: 'See all your projects, tasks, and metrics at a glance with a clean, modern dashboard.',
    bg: 'linear-gradient(135deg, #5634BA, #560DDE)',
  },
  {
    icon: '✅',
    title: 'Task Management',
    desc: 'Create, assign, and track tasks with status badges and real-time updates.',
    bg: 'linear-gradient(135deg, #96A80D, #16FF4B)',
  },
  {
    icon: '🌙',
    title: 'Dark Mode',
    desc: 'A beautiful dark theme with animated gradients for comfortable late-night work sessions.',
    bg: 'linear-gradient(135deg, #C914C7, #560DDE)',
  },
  {
    icon: '📱',
    title: 'Fully Responsive',
    desc: 'Works beautifully on desktop, tablet, and mobile so you can manage on the go.',
    bg: 'linear-gradient(135deg, #922B2B, #AF3F00)',
  },
  {
    icon: '🔒',
    title: 'Secure & Private',
    desc: 'Role-based access ensures your data stays secure and only visible to the right people.',
    bg: 'linear-gradient(135deg, #316D70, #5634BA)',
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
  padding: 5rem 1.5rem 4rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}

.hero__badge {
  display: inline-block;
  padding: 0.4rem 1rem;
  border-radius: 9999px;
  font-size: 0.8rem;
  font-weight: 600;
  background: rgba(86, 52, 186, 0.1);
  color: #5634BA;
  border: 1px solid rgba(86, 52, 186, 0.2);
  margin-bottom: 1.5rem;
}

:global(.dark) .hero__badge {
  background: rgba(72, 198, 203, 0.1);
  color: #48C6CB;
  border-color: rgba(72, 198, 203, 0.2);
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
  box-shadow: 0 16px 48px rgba(86, 52, 186, 0.12);
}

:global(.dark) .feature-card:hover {
  box-shadow: 0 16px 48px rgba(72, 198, 203, 0.12);
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
  background: linear-gradient(135deg, rgba(86, 52, 186, 0.08), rgba(72, 198, 203, 0.08));
  border: 1px solid var(--wayfs-border);
  border-radius: 1.5rem;
  padding: 4rem 2rem;
}

:global(.dark) .cta__content {
  background: linear-gradient(135deg, rgba(86, 52, 186, 0.15), rgba(72, 198, 203, 0.1));
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

/* Responsive */
@media (max-width: 768px) {
  .hero {
    grid-template-columns: 1fr;
    padding: 3rem 1.5rem 2rem;
    text-align: center;
  }

  .hero__title {
    font-size: 2.25rem;
  }

  .hero__subtitle {
    margin-left: auto;
    margin-right: auto;
  }

  .hero__actions {
    justify-content: center;
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
