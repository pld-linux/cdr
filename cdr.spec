Summary:	Easy Tool for automagic CD-> mp3 conversion
Summary(pl):	�atwe narz�dzie do automatycznej konwersji CD-> mp3.
Name:		cdr
Version:	3.0.0
Release:	0
License:	GPL
Group:		Applications
Vendor:		David Cantrell (david@burdell.org)
#Icon:		-
Source0:	http://telia.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-fix-program-locations.patch
URL:		http://cdr.sourceforge.net
#BuildRequires:	-
#PreReq:		-
Requires:	/usr/bin/id3ed
Requires:	/usr/bin/cdparanoia
Requires:	/usr/bin/lame
Requires:	/usr/bin/cdialog
Requires:	/bin/rm
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cdr is a Perl program that provides a simple console front-end to creating high-quality MP3s.  Since cdr is a frontend, it requires many programs in order to do its work. Normally cdr comes with most of the tools you'll need, but since we have them in our distro they are not compiled/provided w/ this package.
Don't forget to set +r on /dev/cdrom for your lusers :-)

%description -l pl
Cdr jest skryptem Perl u�atwiaj�cym tworzenie plik�w mp3 z p�ytek CD. Jest to tylko mi�dzymordzie wymagaj�ce innych narz�dzi, normalnie przychodz� one w paczce z cdr, jednak mamy te narz�dzia w naszych zasobach i dlatego nie znajdziesz ich w tej paczce.
Nie zapomnij ustawi� +r do /dev/cdrom dla Twoich u�ytkownik�w.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/bin/

install cdr.pl $RPM_BUILD_ROOT/usr/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO README PLATFORMS PATCHES LICENSE Changelog
%attr(755,root,root) %{_bindir}/%{name}.pl
