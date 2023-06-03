function initialize() {
    alert(
      "To see the title of a marker, hover over the marker but don't click."
    );
    var myLatlng = new google.maps.LatLng(37.39361, -122.099263);
    var mapOptions = {
      zoom: 5,
      center: myLatlng,
      mapTypeId: google.maps.MapTypeId.ROADMAP,
    };
    var map = new google.maps.Map(
      document.getElementById("map_canvas"),
      mapOptions
    );

    i = 0;
    var markers = [];
    for (pos in myData) {
      i = i + 1;
      var row = myData[pos];
      window.console && console.log(row);
      // if ( i < 3 ) { alert(row); }
      var newLatlng = new google.maps.LatLng(row[0], row[1]);
      var marker = new google.maps.Marker({
        position: newLatlng,
        map: map,
        title: row[2],
      });
      markers.push(marker);
    //   <!-- New options for MarkerClusterer function to display markers -->
      var options = {
        imagePath:
          "http://rawgit.com/googlemaps/js-marker-clusterer/gh-pages/images/m",
      };
    }
    // <!-- New var -->
    var markerCluster = new MarkerClusterer(map, markers, options);
  }