Summary:	A simple program which provides a "run program" window
Summary(pl.UTF-8):	Prosty program prezentujący okienko "uruchom"
Name:		gmrun
Version:	0.9.2
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gmrun/%{name}-%{version}.tar.gz
# Source0-md5:	6cef37a968006d9496fc56a7099c603c
Patch0:		%{name}-gcc4.3.patch
Patch1:		%{name}-gtkcompeltionline.patch
URL:		http://sourceforge.net/projects/gmrun/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple program which provides a "run program" window, featuring a
bash-like TAB completion. It uses GTK+ interface. Also, supports
CTRL-R / CTRL-S / "!" for searching through history. Running commands
in a terminal with CTRL-Enter. URL handlers.

%description -l pl.UTF-8
Prosty program udostępniający okienko "uruchom program", obsługuje
dopełnianie TAB-em. Wykorzystuje interfejs GTK+. Wspiera również
przeszukiwanie historii przy użyciu kombinacji CTRL-R / CTRL-S / "!".
Obsługuje uruchamianie komend w oknie terminala przy użyciu
CTRL-Enter. Odnośniki URL.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
# Disable check for STLport due to bug: http://bugs.gentoo.org/164339
%{__sed} -i -e 's,^AC_PATH_STLPORT,dnl REMOVED ,g' configure.in
%{__sed} -i -e 's,@STLPORT_[A-Z]\+@,,g' src/Makefile.am

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/%{name}/gmrunrc
