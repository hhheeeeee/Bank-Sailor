import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router";
import VueApexCharts from "vue3-apexcharts";

import { defineRule } from "vee-validate";
import { required, email, min } from "@vee-validate/rules";
defineRule("required", required);
defineRule("email", email);
defineRule("min", min);

const app = createApp(App);
const pinia = createPinia();

pinia.use(piniaPluginPersistedstate);
// app.use(createPinia())
app.use(pinia);
app.use(router);
app.use(VueApexCharts);

app.mount("#app");
