%define	name	poedit
%define	version	1.3.6
%define release	%mkrel 3

%define	section	More Applications/Editors
%define	title	Poedit

%define	Summary	Gettext translation file editor

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
License:	MIT
Group:		Editors
URL:		http://www.poedit.org
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:      %_tmppath/%{name}-%{version}-buildroot
Requires:	gettext
BuildRequires:	wxgtku-devel >= 2.8
BuildRequires:	libdb4.5-devel
BuildRequires:	gtkspell-devel
BuildRequires:	zip
BuildRequires:	desktop-file-utils
Requires(Pre):	shared-mime-info
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
poEdit is cross-platform gettext catalogs (.po files) editor. It is built with
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
%__rm -rf %{buildroot}
%makeinstall_std


# menu
%__mkdir_p %buildroot%_menudir
cat > %buildroot%_menudir/%name << EOF
?package(%name): \
command="%_bindir/%name" \
needs="X11" \
icon="%name.png" \
section="%section" \
title="%title" \
mimetypes="application/x-po,application/x-gettext,application/x-gettext-translation,text/x-gettext-translation,text/x-gettext-translation-template" \
accept_url="true" \
multiple_files="true" \
longtitle="%Summary" \
xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GNOME" \
  --add-category="X-MandrivaLinux-MoreApplications-Editors;TextEditor" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


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
%{_menudir}/%{name}
%{_iconsdir}/*
%{_mandir}/man1/*
%{_datadir}/poedit/help/*
%{_datadir}/poedit/icons/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*



