Summary:	Easy Tool for automagic CD-> mp3 conversion
Summary(pl):	£atwe narzêdzie do automatycznej konwersji CD-> mp3.
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
aqq

%description -l pl
aqq

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/bin/

install cdr.pl $RPM_BUILD_ROOT/usr/bin/

%clean

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc TODO README PLATFORMS PATCHES LICENSE Changelog
%attr(755,root,root) %{_bindir}/%{name}.pl
