import { createRouter, createWebHashHistory } from "vue-router";
import homepage from "../components/homepage.vue";
import AboutPage from "../components/about.vue";

const routes = [
  { path: "/", component: homepage },
  { path: "/about", component: AboutPage },
  // Add more routes as needed
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
