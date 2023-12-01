<template>
  <div>
    <h2>About Us</h2>

    <div class="card">
      <img src="https://via.placeholder.com/150" alt="Team Member" />
      <div class="card-body">
        <h3>John Doe</h3>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget
          turpis ac leo pulvinar.
        </p>
      </div>
    </div>

    <div class="card">
      <img src="https://via.placeholder.com/150" alt="Team Member" />
      <div class="card-body">
        <h3>Jane Doe</h3>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget
          turpis ac leo pulvinar.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AboutPage",
};
</script>

<style scoped>
/* Add your styles here */

h2 {
  text-align: center;
}

.card {
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 20px;
  overflow: hidden;
  max-width: 300px;
  transition: transform 0.3s;
}

.card:hover {
  transform: scale(1.05);
}

.card img {
  width: 100%;
  height: auto;
  border-bottom: 1px solid #ccc;
}

.card-body {
  padding: 16px;
}

h3 {
  margin-top: 0;
}
</style>
