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

// Example usage:
setGaugeValue(gaugeElement, 0.3);


const FollowerCount = 0;
const FollowingCount = 0;
const PostCount = 0;
const defaultProfileBio = '';
const dateOfJoining = '';
const privateaccount ='False';
// Update HTML content with JavaScript variables
document.getElementById('followerCount').innerText = FollowerCount;
document.getElementById('followingCount').innerText = FollowingCount;
document.getElementById('postCount').innerText = PostCount;
document.getElementById('profileBio').innerText = defaultProfileBio;
document.getElementById('dateOfJoining').innerText = dateOfJoining;
document.getElementById('privateaccount').innerText = privateaccount;



document.addEventListener('DOMContentLoaded', function() {
    const searchButton = document.querySelector('.buttonFilled');
    const usernameInput = document.querySelector('.app-component-textinput');

    searchButton.addEventListener('click', function() {
        const username = usernameInput.value;
        const usernameDisplay = document.querySelector('.username-display');
        usernameDisplay.textContent = username;
    });
});


document.addEventListener('DOMContentLoaded', function() {
    // Get all navigation links
    const navLinks = document.querySelectorAll('.home-links span');
  
    // Add click event listener to each navigation link
    navLinks.forEach(function(link) {
      link.addEventListener('click', function() {
        // Get the target section id from the data-target attribute
        const targetId = this.getAttribute('data-target');
        // Find the target section by its id
        const targetSection = document.getElementById(targetId);
        // Scroll to the target section smoothly
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


