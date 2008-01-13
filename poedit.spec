Summary:	Gettext translation file editor
Name:		poedit
Version:	1.3.9
Release:	%mkrel 2
License:	MIT
Group:		Editors
URL:		http://www.poedit.net
Source0:	http://nchc.dl.sourceforge.net/sourceforge/poedit/%{name}-%{version}.tar.gz
Patch0:		poedit-1.3.9-fix-desktop-file.patch
BuildRoot:      %_tmppath/%{name}-%{version}-buildroot
Requires:	gettext
BuildRequires:	wxgtku-devel >= 2.8
BuildRequires:	libdb4.6-devel
BuildRequires:	gtkspell-devel
BuildRequires:	zip
Requires(Pre):	shared-mime-info
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
Poedit is cross-platform gettext catalogs (.po files) editor. It is built with
wxWindows toolkit and can run on Unix or Windows. It aims to provide convenient
way of editing gettext catalogs. It features UTF-8 support, fuzzy and
untranslated records highlighting, whitespaces highlighting, references
browser, headers editing and can be used to create new catalogs or update
existing catalogs from source code by single click.

%prep
%setup -q
%patch0 -p0

%build
# wx-config is brain-damaged. Damn you, multiarch, damn you
%configure2_5x --with-wx-config=%{_bindir}/wx-config-unicode
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

# remove files not bundled
%__rm -f %{buildroot}/%{_iconsdir}/poedit.xpm

# (Abel) 1.3.3-1mdk Fix(?) locale file paths
pushd %{buildroot}%{_datadir}/locale
%__mv af_ZA af
%__mv zh_CN zh
%__mv zh_TW zh
%__mv sq_AL sq
popd

%find_lang %{name}

%post
%update_menus
%update_desktop_database

%postun
%clean_menus
%clean_desktop_database

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS README AUTHORS COPYING TODO docs/technote.txt
%dir %{_datadir}/poedit
%{_bindir}/poedit
%{_iconsdir}/*
%{_mandir}/man1/*
%{_datadir}/poedit/help/*
%{_datadir}/poedit/icons/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
