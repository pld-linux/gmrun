#
# TODO
# it links with:
# -lgtk-x11-2.0 -lgdk-x11-2.0 -latk-1.0 -lgdk_pixbuf-2.0 -lpangocairo-1.0 -lgio-2.0 -lXext -lXrender -lXinerama -lXi -lXrandr -lXcursor -lXcomposite -lXdamage -lcairo -lpangoft2-1.0 -lX11 -lXfixes -lpango-1.0 -lm -lfreetype -lz -lfontconfig -lgobject-2.0 -lgmodule-2.0 -lglib-2.0    -lpopt
# so find all BRs ;)

Summary:	A simple program which provides a "run program" window
Summary(pl.UTF-8):	Prosty program prezentujący okienko "uruchom"
Name:		gmrun
Version:	0.9.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gmrun/%{name}-%{version}.tar.gz
# Source0-md5:	6cef37a968006d9496fc56a7099c603c
Patch0:		%{name}-gcc4.3.patch
URL:		http://sourceforge.net/projects/gmrun/
BuildRequires:	gtk+2-devel
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
%patch0 -p1

%build
%configure2_13 \
	--prefix=%{_prefix} \
	--disable-stlport

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
