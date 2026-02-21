<template>
  <div class="page-container">
    <div class="page-header animate-fade-in">
      <h1 class="section-title">👤 Profile</h1>
      <p class="section-subtitle">Your personal account details and public appearance</p>
    </div>

    <div class="profile-card card-wayfs animate-fade-in-delay-1">
      <div class="profile-hero">
        <div class="avatar-large">A</div>
        <div class="profile-info">
          <h2 class="profile-name">Aboubakr</h2>
          <p class="profile-email">aboubakr@wayffs.com</p>
          <div class="profile-badges">
            <span class="badge badge-done">Admin</span>
            <span class="badge badge-progress">Premium</span>
          </div>
        </div>
      </div>
      
      <div class="profile-bio">
        <h3 class="bio-title">About Me</h3>
        <p class="bio-text">Dedicated project manager focused on streamlining workflows and increasing team efficiency. Lover of clean code and green gradients.</p>
      </div>

      <div class="profile-stats">
        <div class="p-stat">
          <div class="p-stat-val">42</div>
          <div class="p-stat-lbl">Projects</div>
        </div>
        <div class="p-stat">
          <div class="p-stat-val">156</div>
          <div class="p-stat-lbl">Tasks</div>
        </div>
        <div class="p-stat">
          <div class="p-stat-val">12</div>
          <div class="p-stat-lbl">Teams</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.profile-card {
  max-width: 600px;
  padding: 2.5rem;
}

.profile-hero {
  display: flex;
  align-items: center;
  gap: 2rem;
  margin-bottom: 2rem;
}

.avatar-large {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: linear-gradient(135deg, #0D9647, #10B860);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  font-weight: 800;
  color: #fff;
  box-shadow: 0 8px 24px rgba(13, 150, 71, 0.3);
}

.profile-name {
  font-size: 1.75rem;
  font-weight: 800;
  color: var(--wayfs-text);
  margin-bottom: 0.25rem;
}

.profile-email {
  color: var(--wayfs-text-secondary);
  font-size: 1rem;
  margin-bottom: 0.75rem;
}

.profile-badges {
  display: flex;
  gap: 0.5rem;
}

.profile-bio {
  margin-bottom: 2rem;
}

.bio-title {
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.bio-text {
  font-size: 0.95rem;
  color: var(--wayfs-text-secondary);
  line-height: 1.6;
}

.profile-stats {
  display: flex;
  justify-content: space-around;
  padding-top: 2rem;
  border-top: 1px solid var(--wayfs-border);
}

.p-stat {
  text-align: center;
}

.p-stat-val {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--wayfs-text);
}

.p-stat-lbl {
  font-size: 0.8rem;
  color: var(--wayfs-text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

@media (max-width: 480px) {
  .profile-hero {
    flex-direction: column;
    text-align: center;
  }
}
</style>
