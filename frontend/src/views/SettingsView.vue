<template>
  <div class="page-container">
    <div class="page-header animate-fade-in">
      <h1 class="section-title">⚙️ Settings</h1>
      <p class="section-subtitle">Manage your account preferences and application settings</p>
    </div>

    <div class="settings-grid">
      <!-- Profile Section -->
      <section class="settings-section card-wayfs animate-fade-in-delay-1">
        <h2 class="settings-section__title">User Profile</h2>
        <div class="settings-form">
          <div class="form-group">
            <label class="label-wayfs">Full Name</label>
            <input type="text" class="input-wayfs" placeholder="Enter your full name">
          </div>
          <div class="form-group">
            <label class="label-wayfs">Email Address</label>
            <input type="email" class="input-wayfs" placeholder="Enter your email">
          </div>
          <button class="btn-wayfs btn-primary">Save Changes</button>
        </div>
      </section>

      <!-- Preferences Section -->
      <section class="settings-section card-wayfs animate-fade-in-delay-2">
        <h2 class="settings-section__title">Preferences</h2>
        <div class="settings-options">
          <div class="option-item">
            <div class="option-info">
              <span class="option-label">Email Notifications</span>
              <span class="option-desc">Receive updates about your projects via email</span>
            </div>
            <div class="toggle-switch"></div>
          </div>
          <div class="option-item">
            <div class="option-info">
              <span class="option-label">Weekly Reports</span>
              <span class="option-desc">Get a summary of your team's progress every week</span>
            </div>
            <div class="toggle-switch toggle-switch--active"></div>
          </div>
        </div>
      </section>

      <!-- Danger Zone -->
      <section class="settings-section card-wayfs animate-fade-in-delay-3 accent-danger">
        <h2 class="settings-section__title text-gradient-danger">Danger Zone</h2>
        <p class="section-desc">Once you delete your account, there is no going back. Please be certain.</p>
        <button class="btn-wayfs btn-danger">Delete Account</button>
      </section>
    </div>
  </div>
</template>

<style scoped>
.page-header {
  margin-bottom: 2rem;
}

.settings-grid {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  max-width: 800px;
}

.settings-section {
  padding: 1.5rem;
}

.settings-section__title {
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 1.25rem;
  color: var(--wayfs-text);
}

.settings-form {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.settings-options {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.option-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.option-info {
  display: flex;
  flex-direction: column;
}

.option-label {
  font-weight: 600;
  color: var(--wayfs-text);
}

.option-desc {
  font-size: 0.85rem;
  color: var(--wayfs-text-secondary);
}

.toggle-switch {
  width: 44px;
  height: 22px;
  background: var(--wayfs-border);
  border-radius: 9999px;
  position: relative;
  cursor: pointer;
  transition: background 0.3s ease;
}

.toggle-switch::after {
  content: '';
  position: absolute;
  left: 2px;
  top: 2px;
  width: 18px;
  height: 18px;
  background: #fff;
  border-radius: 50%;
  transition: transform 0.3s ease;
}

.toggle-switch--active {
  background: #10B860;
}

.toggle-switch--active::after {
  transform: translateX(22px);
}

.section-desc {
  font-size: 0.9rem;
  color: var(--wayfs-text-secondary);
  margin-bottom: 1rem;
}

.accent-danger {
  border-left: 4px solid #C13A2A;
}
</style>
