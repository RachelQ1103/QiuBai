/**
 * Created by Rachel on 16/3/14.
 */

$(document).ready(function() {
    
    console.log( "hello world" );

    var setup = function() {
        // click on Login or Signup
        $('.Qiu-login-sign').on('click', function(){
            var self = $(this);
            console.log('click a');
            $('.disabled').removeClass('disabled');
            self.closest('.Qiu-account-form').addClass('disabled');
        });
    };

    var __main = function(){
         // header-logo will be changed according to weekdays
        var date = new Date();
        var day=date.getDay();
        $('#logo-weekday').src = {{url_for('static/logo', filename='week'+day+'.png')}};

        setup();
    };

    __main();
});



