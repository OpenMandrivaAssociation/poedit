%global wxver 3.2

Summary:	Gettext translation file editor
Name:		poedit
Version:	3.5
Release:	1
License:	MIT
Group:		Editors
URL:		https://www.poedit.net
Source0:	https://github.com/vslavik/poedit/releases/download/v%{version}-oss/poedit-%{version}.tar.gz

BuildRequires:	gettext
BuildRequires:	boost-devel
BuildRequires:	cld2-devel
BuildRequires:	db-devel
BuildRequires:	%{_lib}wxu%{wxver}-devel
BuildRequires:	pkgconfig(cpprest)
BuildRequires:	pkgconfig(gtkspell3-3.0)
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(liblucene++)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(pugixml)
BuildRequires:	wxgtk-devel
BuildRequires:	zip

%description
Poedit is cross-platform gettext catalogs (.po files) editor. It is built with
wxWindows toolkit and can run on Unix or Windows. It aims to provide convenient
way of editing gettext catalogs. It features UTF-8 support, fuzzy and
untranslated records highlighting, whitespaces highlighting, references
browser, headers editing and can be used to create new catalogs or update
existing catalogs from source code by single click.

%files -f %{name}.lang
%license COPYING
%doc NEWS README.md AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*%{name}*.desktop
%{_iconsdir}/hicolor/*/apps/*%{name}*.png
%{_iconsdir}/hicolor/*/apps/*Poedit*.svg
%{_metainfodir}/net.%{name}.Poedit.appdata.xml
%{_mandir}/man1/%{name}.1.*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
export WXRC=/usr/bin/wxrc-%{wxver}
%configure --with-wx-config=%{_libdir}/wx/config/gtk3-unicode-%{wxver}
%make_build

%install
%make_install

# locales
%find_lang %{name}

