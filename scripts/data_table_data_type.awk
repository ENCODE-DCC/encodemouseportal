BEGIN{
    trans=0;
    non=0;
}
{
    if ( $0 ~ /'transcription'/) {
        trans+=10;
        print "insert into MEPages_datatabledatatype values (/" $5 "/" $5 "2," trans ");";
    }
    else {
        non+=10;
        print "insert into MEPages_datatabledatatype values (/" $5 "/" $5 "1," non ");";
    }
}
END{}
