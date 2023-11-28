<!-- <script setup>
import { ref } from "vue";
const msg = ref("Hello World!");
const currentTime = ref("");
const messages = ref(["Message 1", "Message 2"]);
const newMessage = ref("");
const showTime = () => {
  const now = new Date();
  const hours = now.getHours();
  const minutes = now.getMinutes();
  const seconds = now.getSeconds();
  currentTime.value = `${hours}:${minutes}:${seconds}`;
};

const addMessage = () => {
  if (newMessage.value.trim() !== "") {
    messages.value.push(newMessage.value);
    newMessage.value = "";
  }
};

const editMessage = (index) => {
  const editedMessage = prompt("Edit message:", messages.value[index]);
  if (editedMessage !== null) {
    messages.value[index] = editedMessage;
  }
};

const deleteMessage = (index) => {
  const confirmDelete = confirm(
    "Are you sure you want to delete this message?"
  );
  if (confirmDelete) {
    messages.value.splice(index, 1);
  }
};
</script>

<template>
  <div>
    <h1>{{ msg }}</h1>
    <input v-model="msg" />
    <button @click="showTime">Get Time</button>
    <p>Show Time: {{ currentTime }}</p>

    <h2>Messages:</h2>
    <ul>
      <li v-for="(message, index) in messages" :key="index">
        {{ message }}
        <button @click="editMessage(index)">Edit</button>
        <button @click="deleteMessage(index)">Delete</button>
      </li>
    </ul>
    <div>
      <input v-model="newMessage" placeholder="New message" />
      <button @click="addMessage">Add Message</button>
    </div>
  </div>
</template> -->
