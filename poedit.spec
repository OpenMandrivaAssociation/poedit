Summary:	Gettext translation file editor
Name:		poedit
Version:	2.4
Release:	1
License:	MIT
Group:		Editors
URL:		http://www.poedit.net
Source0:	https://github.com/vslavik/poedit/releases/download/v%{version}-oss/poedit-%{version}.tar.gz

Requires:	gettext
BuildRequires:	wxgtku3.0-devel
BuildRequires:	db-devel
BuildRequires:	gtkspell3-devel
BuildRequires:	zip
BuildRequires:	desktop-file-utils
BuildRequires:	boost-devel
BuildRequires:	lucene++-devel
Requires(pre):	shared-mime-info

%description
Poedit is cross-platform gettext catalogs (.po files) editor. It is built with
wxWindows toolkit and can run on Unix or Windows. It aims to provide convenient
way of editing gettext catalogs. It features UTF-8 support, fuzzy and
untranslated records highlighting, whitespaces highlighting, references
browser, headers editing and can be used to create new catalogs or update
existing catalogs from source code by single click.

%prep
%setup -q

%build
%configure --disable-legacytm
%make_build

%install
%make_install

# remove files not bundled
rm -f %{buildroot}%{_iconsdir}/poedit.xpm

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS README AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_metainfodir}/net.%{name}.Poedit.appdata.xml
%{_datadir}/applications/*%{name}*.desktop
%{_iconsdir}/hicolor/*/apps/*%{name}*.png
%{_mandir}/man1/%{name}.1.*

