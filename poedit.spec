Summary:	Gettext translation file editor
Name:		poedit
Version:	2.2
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
Requires(Pre):	shared-mime-info

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
# wx-config is brain-damaged. Damn you, multiarch, damn you
%configure2_5x --disable-legacytm
%make

%install
%makeinstall_std

desktop-file-install \
  --add-category="GTK;GNOME;" \
  --dir=%{buildroot}%{_datadir}/applications \
   %{buildroot}%{_datadir}/applications/net.poedit.Poedit.desktop

# remove files not bundled
rm -f %{buildroot}/%{_iconsdir}/poedit.xpm

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS README AUTHORS
%dir %{_datadir}/poedit
%{_bindir}/poedit
%{_iconsdir}/*
%{_mandir}/man1/*
%dir %{_datadir}/poedit/icons
%{_datadir}/poedit/icons/*
%{_datadir}/applications/*.desktop
%{_datadir}/appdata/*.xml
%{_datadir}/pixmaps/*


