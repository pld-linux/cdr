Summary:	Easy Tool for automagic CD-> MP3 conversion
Summary(pl.UTF-8):   Łatwe narzędzie do automatycznej konwersji CD-> MP3
Name:		cdr
Version:	3.0.0
Release:	0
License:	GPL v2
Vendor:		David Cantrell <david@burdell.org>
Group:		Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	d00f2d00e117f376bff9f72ef50ba166
Patch0:		%{name}-fix-program-locations.patch
URL:		http://cdr.sourceforge.net/
Requires:	/usr/bin/cdialog
Requires:	/usr/bin/cdparanoia
Requires:	/usr/bin/id3ed
Requires:	/usr/bin/lame
Requires:	/bin/rm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cdr is a Perl program that provides a simple console front-end for
creating high-quality MP3s. Since cdr is a frontend, it requires many
programs in order to do its work. Normally cdr comes with most of the
tools you'll need, but since we have them in our distro they are not
compiled/provided w/ this package. Don't forget to set +r on
/dev/cdrom for your lusers :-)

%description -l pl.UTF-8
Cdr jest skryptem Perl ułatwiającym tworzenie plików MP3 z płytek CD.
Jest to tylko interfejs wymagający innych narzędzi, normalnie
przychodzą one w paczce z cdr, jednak mamy te narzędzia w naszych
zasobach i dlatego nie ma ich w tym pakiecie. Nie należy zapomnieć o
ustawieniu +r do /dev/cdrom dla swoich użytkowników.

%prep
%setup -q
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install cdr.pl $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO README PLATFORMS PATCHES LICENSE Changelog
%attr(755,root,root) %{_bindir}/%{name}.pl
