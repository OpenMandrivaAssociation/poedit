Summary:	Gettext translation file editor
Name:		poedit
Version:	1.6.7
Release:	1
License:	MIT
Group:		Editors
URL:		http://www.poedit.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Requires:	gettext
BuildRequires:	wxgtku-devel >= 2.8
BuildRequires:	db-devel
BuildRequires:	gtkspell-devel
BuildRequires:	zip
BuildRequires:	desktop-file-utils
BuildRequires:	boost-devel
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
%configure2_5x --with-wx-config=%{_bindir}/wx-config-unicode
%make

%install
%makeinstall_std

desktop-file-install \
  --add-category="GTK;GNOME;" \
  --dir=%{buildroot}%{_datadir}/applications \
   %{buildroot}%{_datadir}/applications/%{name}.desktop

# remove files not bundled
rm -f %{buildroot}/%{_iconsdir}/poedit.xpm

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS README AUTHORS TODO 
%dir %{_datadir}/poedit
%{_bindir}/poedit
%{_iconsdir}/*
%{_mandir}/man1/*
%{_datadir}/poedit/icons/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*


