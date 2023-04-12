<template>
    <form id="movieForm" @submit.prevent="saveMovie">

        <div class="form-group">
            <label for="title" class="form-label">Movie Title</label>
            <br>
            <input id="title" type="text" name="title" class="form-control"/>
            <br>
        </div>   
        <div class="form-group">
            <label for="description" class="form-label2"> Description </label>
            <br>
            <textarea id="desc" name="description" rows="5" cols="70"></textarea>
            <br>
        </div> 
        <div class="form-group3">
            <label for="poster" class="form-label3"> Image for Poster </label>
            <input id="img" type="file" name="poster"/>
            <br>
        </div>
        
        <br><button type="submit" value="submit"> Submit </button>
    
    </form>
</template>

<script setup>
    import {ref, onMounted} from "vue";

    onMounted(() => {
    getCsrfToken();
    })

    let csrf_token = ref("");

    function getCsrfToken(){
        
        fetch('/api/v1/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                csrf_token.value = data.csrf_token;
            })
    }

    function saveMovie(){
        let movieForm = document.getElementById('movieForm');
        let form_data = new FormData(movieForm);

        fetch("/api/v1/movies", {
            method:'POST',
            body: form_data,
            headers:{
                'X-CSRFTOKEN': csrf_token.value
            }
        })

        .then(function(response){
            return response.json();
        })

        .then(function(data){
            //display a success message
           	console.log(data);
        })

        .catch(function(error){
            console.log(error);
        });
}
</script>

