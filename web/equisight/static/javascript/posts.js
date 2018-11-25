
function screenshot(file_name) {
  console.log(file_name)
  axios.post('/screen_shot', {
    file_name: file_name
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });


//   $.ajax({
//     type: 'POST',
//     url: '/screen_shot',
//     data:JSON.stringify(file_name),
//     success: function (response) {
//         alert("Data added successfully");
//      },    
// });
}
