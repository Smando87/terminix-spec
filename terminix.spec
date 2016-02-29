Summary: A tiling terminal emulator based on GTK+ 3
Name:terminix
Version: 0.51.0
Release: 1%{dist}
License: MPL
Group: Applications/Utilities

Source: https://github.com/gnunn1/terminix/releases/download/%{version}/terminix.zip
URL: http://github.com/gnunn1/terminix

BuildRequires: gtk3-devel
BuildRequires: vte3-devel
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: dconf

Requires: gtk3
Requires: vte3
Requires: gsettings-desktop-schemas
Requires: dconf

Packager: Asif Ali Rizvan <fast.rizwaan@gmail.com>

%description
A tiling terminal emulator

%prep
exit 0

%build
exit 0

%install
unzip -x -d %buildroot %{SOURCE0} 

%files
%defattr(755,root,root)
%{_bindir}/terminix        
%{_datadir}/applications/com.gexperts.Terminix.desktop
%attr(644,root,root)  
%{_datadir}/terminix/schemes/tango.json  
%{_datadir}/terminix/schemes/solarized-light.json  
%{_datadir}/terminix/schemes/solarized-dark.json  
%{_datadir}/terminix/schemes/orchis.json  
%{_datadir}/terminix/schemes/linux.json  
%{_datadir}/terminix/resources/terminix.gresource  
%{_datadir}/glib-2.0/schemas/com.gexperts.Terminix.gschema.xml  
/usr/share/dbus-1/services/com.gexperts.Terminix.service
/usr/share/locale/de/LC_MESSAGES/terminix.mo
/usr/share/locale/en/LC_MESSAGES/terminix.mo
/usr/share/locale/fr/LC_MESSAGES/terminix.mo
/usr/share/locale/pt_BR/LC_MESSAGES/terminix.mo
/usr/share/locale/zh_CN/LC_MESSAGES/terminix.mo
/usr/share/locale/zh_TW/LC_MESSAGES/terminix.mo
/usr/share/nautilus-python/extensions/open-terminix.py
/usr/share/nautilus-python/extensions/open-terminix.pyc
/usr/share/nautilus-python/extensions/open-terminix.pyo
/usr/share/terminix/schemes/base16-twilight-dark.json
/usr/share/terminix/schemes/monokai.json

%post
/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas/

%postun
/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas/

%changelog
