options symbolgen mprint mlogic mcompilenote=all;

%macro format();
	%do year = 2000 %to 2009;
		libname library "C:\Users\bjsul\Documents\NCSU\MSA\Fall\Visualization\Visualization Project-20191008T021201Z-001\Visualization Project\&year";
		%include "C:\Users\bjsul\Documents\NCSU\MSA\Fall\Visualization\Visualization Project-20191008T021201Z-001\Visualization Project\&year\format91-09.sas";

		data merged&year;
			merge library.accident library.person library.vehicle;
			by st_case;
		run;
		
		proc export data=work.merged&year dbms=csv replace
			outfile="C:\Users\bjsul\Documents\NCSU\MSA\Fall\Visualization\Visualization Project-20191008T021201Z-001\Visualization Project\&year\&year..csv";
		run;
		
		%if &year=2006 or &year=2009 %then %let rows=MAX;
		%else %let rows=20000;
		proc import dbms=csv out=work.year&year replace
			datafile="C:\Users\bjsul\Documents\NCSU\MSA\Fall\Visualization\Visualization Project-20191008T021201Z-001\Visualization Project\&year\&year..csv";
			guessingrows=&rows;
		run;

	%end;
	%do year = 2010 %to 2017;
		libname library "C:\Users\bjsul\Documents\NCSU\MSA\Fall\Visualization\Visualization Project-20191008T021201Z-001\Visualization Project\&year";
		%include "C:\Users\bjsul\Documents\NCSU\MSA\Fall\Visualization\Visualization Project-20191008T021201Z-001\Visualization Project\&year\format%substr(&year, 3, 2).sas";
		data merged&year;
			merge library.accident library.person library.vehicle;
			by st_case;
		run;

		proc export data=work.merged&year dbms=csv replace
			outfile="C:\Users\bjsul\Documents\NCSU\MSA\Fall\Visualization\Visualization Project-20191008T021201Z-001\Visualization Project\&year\&year..csv";
		run;

		proc import dbms=csv out=work.year&year replace
			datafile="C:\Users\bjsul\Documents\NCSU\MSA\Fall\Visualization\Visualization Project-20191008T021201Z-001\Visualization Project\&year\&year..csv";
			guessingrows=20000;
		run;
	%end;
%mend;

%format()

%let year=2017;
