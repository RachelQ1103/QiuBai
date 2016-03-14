/**
 * Created by Rachel on 16/3/14.
 */

$(document).ready(function() {
    
    console.log( "hello world" );
    
    // header-logo will be changed according to weekdays
    var date = new Date();
    var day=date.getDay();
    $("#logo-weekday").attr('src', url_for('/static/logo', filename='week'+day+'.png'));

    var setup = function() {
        // click on Login or Signup
        $(".Qiu-login-sign").on('click', function(){
            var self = $(this);
            console.log('click a');
            $('.active').removeClass('active');
            self.addClass('active');
        });

        // action after clicking
        var clickAction = function (showLogin) {
            $('#Qiu-login-form').toggle(showLogin);
            $('#Qiu-signup-form').toggle(!showLogin);
        };

        $('#Qiu-signup').on('click', function(){
            var showLogin = false;
            clickAction(showLogin);
        });
        $('#Qiu-login').on('click', function(){
            var showLogin = True;
            clickAction(showLogin);
        });
    };

    var __main = function(){
        setup();
        // select login
        $('#Qiu-login').click();
    };

    __main();
});



