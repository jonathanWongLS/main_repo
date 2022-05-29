find_square_root(curval) {
    var low = 0;
    var high = curval;

    var i = 0
    while (true) {
      console.log("looped");
      var est = 2 * (high + low) / 4
      var diff = (est * est) - curval;
      
      diff !== 0 ? diff : 0;

      if (Math.abs(diff) < this.epsilon) {break;}
      if (diff > 0) {high = est;}
      else {low = est;};

      i += Math.random();
    }
    
    this.accumulator = est;
    return est
}