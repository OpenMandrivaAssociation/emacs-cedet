%define fname            cedet

%define cogre_evr        %{epoch}:1.0-%{release}
%define ede_evr          %{epoch}:1.0-%{release}
%define eieio_evr        %{epoch}:1.3-%{release}
%define semantic_evr     %{epoch}:2.0-%{release}
%define speedbar_evr     %{epoch}:1.0.3-%{release}

Name:           emacs-%{fname}
Version:        1.1
Release:        2
Epoch:          0
Summary:        Collection of Emacs Development Environment Tools
License:        GPL
URL:            http://sourceforge.net/projects/cedet/
Source:         https://sourceforge.net/projects/cedet/files/cedet/cedet-%{version}.tar.gz
Group:          Editors
Provides:       cedet = %{epoch}:%{version}-%{release}
Provides:       cogre = %{cogre_evr}
Provides:       emacs-cogre = %{cogre_evr}
Provides:       ede = %{ede_evr}
Provides:       emacs-ede = %{ede_evr}
Provides:       eieio = %{eieio_evr}
Obsoletes:      emacs-eieio < %{eieio_evr}
Provides:       emacs-eieio = %{eieio_evr}
Provides:       semantic = %{semantic_evr}
Obsoletes:      emacs-semantic < %{semantic_evr}
Provides:       emacs-semantic = %{semantic_evr}
Obsoletes:      emacs-speedbar < %{speedbar_evr}
Provides:       speedbar = %{speedbar_evr}
Provides:       emacs-speedbar = %{speedbar_evr}
Requires:       emacs-bin
BuildRequires:  emacs-bin
BuildRequires:  texinfo
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
CEDET is a collection of tools written with the end goal of
creating an advanced development environment in Emacs.

Emacs already is a great environment for writing software, but there
are additional areas that need improvement. Many new ideas for
integrated environments have been developed in newer products, such
as Microsoft's Visual environment, JBuilder, Eclipse, or KDevelop.
CEDET is a project which brings together several different tools
needed to implement advanced features.

%prep
%setup -q -n %{fname}-%{version}
%{_bindir}/find . -type f -name "*.info" | %{_bindir}/xargs %{__rm}

%build
%{__make} clean-autoloads
%{__make} clean-all
%{__make}

%install
%{__rm} -rf %{buildroot}

# cedet-common
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/cedet-common
%{__install} -m 644 common/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/cedet-common
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/cedet-common/icons
%{__install} -m 644 common/icons/*.xpm %{buildroot}%{_datadir}/emacs/site-lisp/cedet-common/icons

# cedet-contrib
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/cedet-contrib
%{__install} -m 644 contrib/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/cedet-contrib
%{__install} -m 644 contrib/*.wy %{buildroot}%{_datadir}/emacs/site-lisp/cedet-contrib

# cogre
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/cogre/templates
%{__install} -m 644 cogre/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/cogre
%{__install} -m 644 cogre/*.xpm %{buildroot}%{_datadir}/emacs/site-lisp/cogre
%{__install} -m 644 cogre/*.wy %{buildroot}%{_datadir}/emacs/site-lisp/cogre
%{__install} -m 644 cogre/templates/*.srt %{buildroot}%{_datadir}/emacs/site-lisp/cogre/templates

# ede
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/ede/templates
%{__install} -m 644 ede/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/ede
%{__install} -m 644 ede/templates/*.srt %{buildroot}%{_datadir}/emacs/site-lisp/ede/templates

# eieio
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/eieio
%{__install} -m 644 eieio/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/eieio

# remove eieio tests
%{__rm} -f %{buildroot}%{_datadir}/emacs/site-lisp/eieio/eieio-tests.el{,c}

# semantic
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/semantic
%{__install} -m 644 semantic/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/semantic
%{__install} -m 644 semantic/*.wy %{buildroot}%{_datadir}/emacs/site-lisp/semantic
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/semantic/bovine
%{__install} -m 644 semantic/bovine/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/semantic/bovine
%{__install} -m 644 semantic/bovine/*.by %{buildroot}%{_datadir}/emacs/site-lisp/semantic/bovine
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/semantic/ctags
%{__install} -m 644 semantic/ctags/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/semantic/ctags
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/semantic/symref
%{__install} -m 644 semantic/symref/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/semantic/symref
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/semantic/wisent
%{__install} -m 644 semantic/wisent/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/semantic/wisent
%{__install} -m 644 semantic/wisent/*.wy %{buildroot}%{_datadir}/emacs/site-lisp/semantic/wisent

# speedbar
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/speedbar
%{__install} -m 644 speedbar/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/speedbar
%{__install} -m 644 speedbar/*.xpm %{buildroot}%{_datadir}/emacs/site-lisp/speedbar

# srecode
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/srecode/templates
%{__install} -m 644 srecode/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/srecode
%{__install} -m 644 srecode/*.wy %{buildroot}%{_datadir}/emacs/site-lisp/srecode
%{__install} -m 644 srecode/templates/* %{buildroot}%{_datadir}/emacs/site-lisp/srecode/templates

# Install symlinks for upstream compat
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/cedet
pushd %{buildroot}%{_datadir}/emacs/site-lisp/cedet
%{__ln_s} ../cedet-common common
%{__ln_s} ../cedet-contrib contrib
%{__ln_s} ../cogre cogre
%{__ln_s} ../ede ede
%{__ln_s} ../eieio eieio
%{__ln_s} ../semantic semantic
%{__ln_s} ../speedbar speedbar
%{__ln_s} ../srecode srecode
popd

# Install startup script
%{__mkdir_p} %{buildroot}%{_sysconfdir}/emacs/site-start.d
%{__cat} > %{buildroot}%{_sysconfdir}/emacs/site-start.d/cedet.el << EOF
;; Load CEDET
(load-file "%{_datadir}/emacs/site-lisp/cedet/common/cedet.el")

;; Enabling various SEMANTIC minor modes. See INSTALL.semantic for more ideas.
;; Select one of the following
(semantic-load-enable-code-helpers)
;; (semantic-load-enable-guady-code-helpers)
;; (semantic-load-enable-excessive-code-helpers)

;; Enable this if you develop in semantic, or develop grammars
;; (semantic-load-enable-semantic-debugging-helpers)
EOF

# Install infopages
%{__mkdir_p} %{buildroot}%{_infodir} 
for info in cogre/cogre.info \
            common/cedet.info \
            ede/ede.info \
            eieio/eieio.info \
            semantic/doc/bovine.info \
            semantic/doc/grammar-fw.info \
            semantic/doc/semantic-appdev.info \
            semantic/doc/semantic.info \
            semantic/doc/semantic-langdev.info \
            semantic/doc/semantic-user.info \
            semantic/doc/wisent.info \
            speedbar/speedbar.info \
            srecode/srecode.info; do
    %{__install} -m 644 ${info} %{buildroot}%{_infodir}
done

# Install docs
for dir in cogre common contrib ede eieio semantic speedbar; do
    for file in ChangeLog INSTALL NEWS ONEWS README; do
        if [ -f ${dir}/${file} ]; then
            %{__install} -m 644 ${dir}/${file} ${file}.${dir}
        fi
    done
done

%clean
%{__rm} -rf %{buildroot}



%files
%defattr(-, root, root)
%doc ChangeLog* INSTALL* *NEWS* PRERELEASE_CHECKLIST README* 
%{_datadir}/emacs/site-lisp/*
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/*.el
%{_infodir}/*.info*


%changelog
* Sun May 15 2011 Lev Givon <lev@mandriva.org> 0:1.0-2mdv2011.0
+ Revision: 674867
- Rebuild for contrib/updates to address parsing problem (#57629).

* Wed Mar 02 2011 Lev Givon <lev@mandriva.org> 0:1.0-1
+ Revision: 641310
- Update to 1.0.
  Include some missing files.

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0:1.0-0.pre7.2mdv2011.0
+ Revision: 610354
- rebuild

* Wed Apr 28 2010 Lev Givon <lev@mandriva.org> 0:1.0-0.pre7.1mdv2010.1
+ Revision: 540431
- Update to 1.0pre7.

* Fri Jun 12 2009 Lev Givon <lev@mandriva.org> 0:1.0-0.pre6.3mdv2010.0
+ Revision: 385572
- Include linemark.el and lmcompile.el in the package.

* Wed Jun 10 2009 Lev Givon <lev@mandriva.org> 0:1.0-0.pre6.2mdv2010.0
+ Revision: 384975
- Install srecode.
- Update to 1.0pre6.

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0:1.0-0.pre4.1mdv2008.1
+ Revision: 136403
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + David Walluck <walluck@mandriva.org>
    - 2.0pre4 (compatible with emacs 22)
    - Import emacs-cedet



* Mon Sep 04 2006 David Walluck <walluck@mandriva.org> 0:1.0-0.pre3.2mdv2007.0
- rebuild to fix release

* Mon Jan 30 2006 David Walluck <walluck@mandriva.org> 0:1.0-0.pre3.1mdk
- release

