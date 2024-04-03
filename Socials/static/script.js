const gaugeElement = document.querySelector(".gauge");

function setGaugeValue(gauge, value) {
    if (value < 0 || value > 1) {
        return;
    }

    gauge.querySelector(".gauge__fill").style.transform = `rotate(${value * 180}deg)`;
    gauge.querySelector(".gauge__cover").textContent = `${Math.round(value * 100)}%`;

    // if (value < 0.5) {
    //     // If the gauge value is less than 0.5, show the alert
    //     Swal.fire({
    //         icon: 'error',
    //         title: 'Low Authenticity Detected',
    //         html: `You can report it to, <a href="https://mumbaipolice.gov.in/OnlineComplaints?ps_id=0" target="_blank"> <span class="underline">Mumbai Police</span></a>, <a href="https://cybercrime.gov.in/Accept.aspx" target="_blank"><span class="underline">CyberCrime Portal</span></a> and <a href="https://www.instagram.com/hacked/" target="_blank"><span class="underline">Instagram Support</span></a>`,
    //         confirmButtonText: 'OK',
          
    //     });
    // }
}


setGaugeValue(gaugeElement, 0.3);


then(response => response.json())
.then(data => {

    const instagramUser = data.instagram_user;
    document.getElementById('followerCount').innerText = instagramUser.followers_count;
    document.getElementById('followingCount').innerText = instagramUser.follows_count;
    document.getElementById('postCount').innerText = instagramUser.posts_count;
    document.getElementById('profileBio').innerText = instagramUser.biography;
    document.getElementById('dateOfJoining').innerText = instagramUser.date_joined;
    document.getElementById('privateaccount').innerText = instagramUser.is_private ? 'Yes' : 'No';
})
.catch(error => {
    console.error('Error:', error);
});


document.addEventListener('DOMContentLoaded', function() {
    const searchButton = document.querySelector('.buttonFilled'); 
    const usernameInput = document.querySelector('.app-component-textinput'); 

    searchButton.addEventListener('click', function(event) {
        event.preventDefault(); 
        const username = usernameInput.value.trim(); 
        if (username !== '') { 
            
            const usernameDisplay = document.querySelector('.username-display');
            usernameDisplay.textContent = username;
        } else {
            
            alert('Please enter a username.');
        }
    });
});


document.addEventListener('DOMContentLoaded', function() {
  
    const navLinks = document.querySelectorAll('.home-links span');
  
    
    navLinks.forEach(function(link) {
      link.addEventListener('click', function() {
       
        const targetId = this.getAttribute('data-target');
      
        const targetSection = document.getElementById(targetId);
     
        targetSection.scrollIntoView({ behavior: 'smooth' });
      });
    });
  });


  function redirectToLoginPage() {
    window.location.href = 'login.html';
}












  document.addEventListener("DOMContentLoaded", function() {
    var usernameInput = document.getElementById("usernameInput");
    var displayedUsername = document.getElementById("displayedUsername");
    var searchButton = document.getElementById("searchButton");

    // Add click event listener to the search button
    searchButton.addEventListener("click", function() {
        // Get the value from the username input
        var newUsername = "@" + usernameInput.value; // Concatenate "@" symbol
       
        // Update the displayed username with the new value
        displayedUsername.textContent = newUsername;
    });
});


