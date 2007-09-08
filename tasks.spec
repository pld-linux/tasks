Summary:	Tiny GNOME tasklist application
Summary(pl.UTF-8):	Mała aplikacja listy zadań dla GNOME
Name:		tasks
Version:	0.11
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://pimlico-project.org/sources/tasks/%{name}-%{version}.tar.gz
# Source0-md5:	9055ac3d6e59118958acbde7bdc407c1
URL:		http://pimlico-project.org/tasks.html
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 1.2
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libsexy-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	pkgconfig
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tasks is a simple To Do list application that eschews complicated
features for a lean interface and functionality that just does the
right thing. It has a simple interface with little cruft around the
list of tasks, is ported to the OpenMoko framework, and there are
plans for focused ports to other frameworks (such as Maemo as used on
the Nokia N800).

%description -l pl.UTF-8
Tasks to mała aplikacja listy zadań, w której zrezygnowano z bardziej
złożonych możliwości dla skromnego interfejsu i funkcjonalności
robiącej to co trzeba. Ma prosty interfejs z małymi sztuczkami przy
liście zadań, jest portowany do środowiska OpenMoko i są plany portów
na inne platformy (takie jak Maemo używane na Nokii N800).

%prep
%setup -q

%build
%{__glib_gettextize}
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/tasks
%{_datadir}/tasks/tasks-ui.xml
%{_desktopdir}/tasks.desktop
%{_iconsdir}/hicolor/*/apps/tasks.png
%{_iconsdir}/hicolor/scalable/apps/tasks.svg
