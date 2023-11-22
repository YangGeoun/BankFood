<template>
    <tr>
        <td>{{ article.author_name }}</td>
        <td>{{ article.title }}</td>
        <td>{{ article.created_at }}</td>
        <td>{{ article.updated_at }}</td>


    </tr>
</template>

<script setup>
import { ref } from 'vue';

defineProps(['article'])

</script>

<style scoped>

</style>