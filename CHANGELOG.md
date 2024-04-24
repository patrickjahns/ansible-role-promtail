# Changelog

## [1.31.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.31.0) (2024-04-24)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.30.0...1.31.0)

**Implemented enhancements:**

- validate templated promtail config file [\#221](https://github.com/patrickjahns/ansible-role-promtail/pull/221) ([patrickjahns](https://github.com/patrickjahns))

## [1.30.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.30.0) (2024-04-24)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.29.1...1.30.0)

**Merged pull requests:**

- chore\(deps\): update dependency grafana/loki to v3 [\#215](https://github.com/patrickjahns/ansible-role-promtail/pull/215) ([renovate[bot]](https://github.com/apps/renovate))

## [1.29.1](https://github.com/patrickjahns/ansible-role-promtail/tree/1.29.1) (2024-04-24)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.29.0...1.29.1)

**Merged pull requests:**

- chore\(deps\): update dependency grafana/loki to v2.9.7 [\#216](https://github.com/patrickjahns/ansible-role-promtail/pull/216) ([renovate[bot]](https://github.com/apps/renovate))
- ci: bumped ansible test versions and base os versions [\#214](https://github.com/patrickjahns/ansible-role-promtail/pull/214) ([patrickjahns](https://github.com/patrickjahns))

## [1.29.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.29.0) (2024-04-08)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.28.0...1.29.0)

**Implemented enhancements:**

- Support arbitrary options in the configuration file [\#203](https://github.com/patrickjahns/ansible-role-promtail/issues/203)
- Add variable \(list\) for additional command line arguments/flags passed to promtail [\#167](https://github.com/patrickjahns/ansible-role-promtail/issues/167)
- feat: add promtail\_extra\_args variable to allow configuring the service arguments [\#207](https://github.com/patrickjahns/ansible-role-promtail/pull/207) ([sfhl](https://github.com/sfhl))

**Fixed bugs:**

- Automatic publishing to Ansible Galaxy is currently broken [\#199](https://github.com/patrickjahns/ansible-role-promtail/issues/199)

**Merged pull requests:**

- chore\(deps\): update dependency grafana/loki to v2.9.6 [\#210](https://github.com/patrickjahns/ansible-role-promtail/pull/210) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency setuptools to v69.2.0 [\#209](https://github.com/patrickjahns/ansible-role-promtail/pull/209) ([renovate[bot]](https://github.com/apps/renovate))

## [1.28.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.28.0) (2024-02-14)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.27.0...1.28.0)

**Merged pull requests:**

- ci: bump python version to 3.10 [\#208](https://github.com/patrickjahns/ansible-role-promtail/pull/208) ([patrickjahns](https://github.com/patrickjahns))
- chore\(deps\): update dependency setuptools to v69.1.0 [\#206](https://github.com/patrickjahns/ansible-role-promtail/pull/206) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency grafana/loki to v2.9.4 [\#202](https://github.com/patrickjahns/ansible-role-promtail/pull/202) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update actions/setup-python action to v5 [\#201](https://github.com/patrickjahns/ansible-role-promtail/pull/201) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency setuptools to v69 [\#200](https://github.com/patrickjahns/ansible-role-promtail/pull/200) ([renovate[bot]](https://github.com/apps/renovate))

## [1.27.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.27.0) (2023-11-05)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.26.0...1.27.0)

**Fixed bugs:**

- promtail\_config\_expand\_env variable is wrong by default [\#187](https://github.com/patrickjahns/ansible-role-promtail/issues/187)
- fix: disable long lines splitting in promtail\_config\_scrape\_configs [\#197](https://github.com/patrickjahns/ansible-role-promtail/pull/197) ([niasar](https://github.com/niasar))
- Updated `config.expand-env` related variable and templating [\#194](https://github.com/patrickjahns/ansible-role-promtail/pull/194) ([azhinu](https://github.com/azhinu))

**Closed issues:**

- unable to parse syslog config receiver  [\#196](https://github.com/patrickjahns/ansible-role-promtail/issues/196)

**Merged pull requests:**

- chore\(deps\): update dependency grafana/loki to v2.9.2 [\#195](https://github.com/patrickjahns/ansible-role-promtail/pull/195) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency setuptools to v68.2.2 [\#191](https://github.com/patrickjahns/ansible-role-promtail/pull/191) ([renovate[bot]](https://github.com/apps/renovate))

## [1.26.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.26.0) (2023-09-14)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.25.0...1.26.0)

**Merged pull requests:**

- chore\(deps\): update dependency grafana/loki to v2.9.1 [\#192](https://github.com/patrickjahns/ansible-role-promtail/pull/192) ([renovate[bot]](https://github.com/apps/renovate))

## [1.25.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.25.0) (2023-09-14)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.24.1...1.25.0)

**Merged pull requests:**

- chore\(deps\): update dependency grafana/loki to v2.9.0 [\#189](https://github.com/patrickjahns/ansible-role-promtail/pull/189) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update actions/checkout action to v4 [\#188](https://github.com/patrickjahns/ansible-role-promtail/pull/188) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency setuptools to v68 [\#183](https://github.com/patrickjahns/ansible-role-promtail/pull/183) ([renovate[bot]](https://github.com/apps/renovate))

## [1.24.1](https://github.com/patrickjahns/ansible-role-promtail/tree/1.24.1) (2023-08-12)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.24.0...1.24.1)

**Merged pull requests:**

- chore\(deps\): update dependency grafana/loki to v2.8.4 [\#184](https://github.com/patrickjahns/ansible-role-promtail/pull/184) ([renovate[bot]](https://github.com/apps/renovate))

## [1.24.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.24.0) (2023-05-12)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.23.1...1.24.0)

**Closed issues:**

- Update release pipeline \(before Jun 23\) [\#163](https://github.com/patrickjahns/ansible-role-promtail/issues/163)

**Merged pull requests:**

- ci: updated release pipeline to fix deprecated github action usages [\#180](https://github.com/patrickjahns/ansible-role-promtail/pull/180) ([patrickjahns](https://github.com/patrickjahns))
- chore\(deps\): update dependency grafana/loki to v2.8.2 [\#176](https://github.com/patrickjahns/ansible-role-promtail/pull/176) ([renovate[bot]](https://github.com/apps/renovate))

## [1.23.1](https://github.com/patrickjahns/ansible-role-promtail/tree/1.23.1) (2023-04-25)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.23.0...1.23.1)

**Merged pull requests:**

- chore\(deps\): update dependency grafana/loki to v2.8.1 [\#174](https://github.com/patrickjahns/ansible-role-promtail/pull/174) ([renovate[bot]](https://github.com/apps/renovate))

## [1.23.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.23.0) (2023-04-05)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.22.3...1.23.0)

**Implemented enhancements:**

- feat: download binaries to ansible controller and copy to nodes [\#128](https://github.com/patrickjahns/ansible-role-promtail/pull/128) ([gannaramu](https://github.com/gannaramu))

**Merged pull requests:**

- chore\(deps\): update dependency grafana/loki to v2.8.0 [\#171](https://github.com/patrickjahns/ansible-role-promtail/pull/171) ([renovate[bot]](https://github.com/apps/renovate))

## [1.22.3](https://github.com/patrickjahns/ansible-role-promtail/tree/1.22.3) (2023-03-31)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.22.2...1.22.3)

**Merged pull requests:**

- chore\(deps\): update dependency grafana/loki to v2.7.5 [\#168](https://github.com/patrickjahns/ansible-role-promtail/pull/168) ([renovate[bot]](https://github.com/apps/renovate))

## [1.22.2](https://github.com/patrickjahns/ansible-role-promtail/tree/1.22.2) (2023-02-25)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.22.1...1.22.2)

**Merged pull requests:**

- chore\(deps\): update dependency grafana/loki to v2.7.4 [\#165](https://github.com/patrickjahns/ansible-role-promtail/pull/165) ([renovate[bot]](https://github.com/apps/renovate))

## [1.22.1](https://github.com/patrickjahns/ansible-role-promtail/tree/1.22.1) (2023-02-20)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.22.0...1.22.1)

**Fixed bugs:**

- Revert back to fetching of version information from localhost [\#162](https://github.com/patrickjahns/ansible-role-promtail/pull/162) ([mprasil](https://github.com/mprasil))

**Closed issues:**

- latest Tag: failing at downloading SHA256SUMS [\#76](https://github.com/patrickjahns/ansible-role-promtail/issues/76)
- \[Discussion\] Add loki installation mechanism \(opt-in, additional to promtail\) [\#58](https://github.com/patrickjahns/ansible-role-promtail/issues/58)

**Merged pull requests:**

- chore\(deps\): update dependency setuptools to v67.3.2 [\#161](https://github.com/patrickjahns/ansible-role-promtail/pull/161) ([renovate[bot]](https://github.com/apps/renovate))
- fix: fail early when using promtail\_binary\_local\_dir [\#158](https://github.com/patrickjahns/ansible-role-promtail/pull/158) ([patrickjahns](https://github.com/patrickjahns))

## [1.22.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.22.0) (2023-02-10)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.21.0...1.22.0)

**Implemented enhancements:**

- feat: add var promtail\_binary\_local\_dir  [\#104](https://github.com/patrickjahns/ansible-role-promtail/pull/104) ([OuiSouss](https://github.com/OuiSouss))

**Merged pull requests:**

- chore\(deps\): update dependency setuptools to v67.2.0 [\#156](https://github.com/patrickjahns/ansible-role-promtail/pull/156) ([renovate[bot]](https://github.com/apps/renovate))

## [1.21.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.21.0) (2023-02-01)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.20.0...1.21.0)

**Implemented enhancements:**

- chore\(deps\): update dependency grafana/loki to v2.7.3 [\#151](https://github.com/patrickjahns/ansible-role-promtail/pull/151) ([renovate[bot]](https://github.com/apps/renovate))

**Closed issues:**

- Reenable version check for default tests [\#135](https://github.com/patrickjahns/ansible-role-promtail/issues/135)

**Merged pull requests:**

- test: fix tox configuration [\#153](https://github.com/patrickjahns/ansible-role-promtail/pull/153) ([patrickjahns](https://github.com/patrickjahns))
- chore\(deps\): update dependency setuptools to v67 [\#152](https://github.com/patrickjahns/ansible-role-promtail/pull/152) ([renovate[bot]](https://github.com/apps/renovate))

## [1.20.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.20.0) (2022-12-10)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.19.2...1.20.0)

**Merged pull requests:**

- chore\(deps\): update dependency grafana/loki to v2.7.1 [\#146](https://github.com/patrickjahns/ansible-role-promtail/pull/146) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency molecule to v4.0.4 [\#145](https://github.com/patrickjahns/ansible-role-promtail/pull/145) ([renovate[bot]](https://github.com/apps/renovate))
- fix\(renovate\): major rewrite by removing duplicates [\#144](https://github.com/patrickjahns/ansible-role-promtail/pull/144) ([MindTooth](https://github.com/MindTooth))

## [1.19.2](https://github.com/patrickjahns/ansible-role-promtail/tree/1.19.2) (2022-11-28)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.19.1...1.19.2)

**Fixed bugs:**

- Remove home parameter in user task [\#143](https://github.com/patrickjahns/ansible-role-promtail/pull/143) ([hafu](https://github.com/hafu))

**Closed issues:**

- 1.19.1 no longer works: user promtail is currently used by process 546 [\#140](https://github.com/patrickjahns/ansible-role-promtail/issues/140)

**Merged pull requests:**

- test: added tests for catching role upgrade issues [\#141](https://github.com/patrickjahns/ansible-role-promtail/pull/141) ([patrickjahns](https://github.com/patrickjahns))
- chore\(deps\): update dependency setuptools to v65.6.3 [\#137](https://github.com/patrickjahns/ansible-role-promtail/pull/137) ([renovate[bot]](https://github.com/apps/renovate))

## [1.19.1](https://github.com/patrickjahns/ansible-role-promtail/tree/1.19.1) (2022-11-25)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.19.0...1.19.1)

**Merged pull requests:**

- Set promtail user home to install directory [\#138](https://github.com/patrickjahns/ansible-role-promtail/pull/138) ([hafu](https://github.com/hafu))

## [1.19.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.19.0) (2022-11-18)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.18.0...1.19.0)

**Implemented enhancements:**

- chore\(deps\): update dependency grafana/loki to v2.7.0 [\#134](https://github.com/patrickjahns/ansible-role-promtail/pull/134) ([renovate[bot]](https://github.com/apps/renovate))
- add var to control promtail config env var expansion [\#132](https://github.com/patrickjahns/ansible-role-promtail/pull/132) ([rplevka](https://github.com/rplevka))

**Closed issues:**

- Make LimitNOFILE in systemd service configurable [\#129](https://github.com/patrickjahns/ansible-role-promtail/issues/129)
- run\_once causes failures when not all nodes in batch get promtail [\#112](https://github.com/patrickjahns/ansible-role-promtail/issues/112)

**Merged pull requests:**

- test: adjust ansible test matrix [\#136](https://github.com/patrickjahns/ansible-role-promtail/pull/136) ([patrickjahns](https://github.com/patrickjahns))
- ci: run in cgroups mode host - fixes systemd issues [\#133](https://github.com/patrickjahns/ansible-role-promtail/pull/133) ([patrickjahns](https://github.com/patrickjahns))
- chore\(deps\): update dependency setuptools to v65 [\#127](https://github.com/patrickjahns/ansible-role-promtail/pull/127) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency molecule to v4.0.1 [\#123](https://github.com/patrickjahns/ansible-role-promtail/pull/123) ([renovate[bot]](https://github.com/apps/renovate))
- fix: delegate fetching of version information to localhost [\#122](https://github.com/patrickjahns/ansible-role-promtail/pull/122) ([patrickjahns](https://github.com/patrickjahns))

## [1.18.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.18.0) (2022-07-19)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.17.0...1.18.0)

**Implemented enhancements:**

- Add variable promtail\_systemd\_service\_template\_file for systemd service template file [\#117](https://github.com/patrickjahns/ansible-role-promtail/pull/117) ([ni-mkougioumtzian](https://github.com/ni-mkougioumtzian))

**Merged pull requests:**

- chore\(deps\): update dependency grafana/loki to v2.6.1 [\#120](https://github.com/patrickjahns/ansible-role-promtail/pull/120) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency molecule-docker to v2 [\#119](https://github.com/patrickjahns/ansible-role-promtail/pull/119) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency setuptools to v63.2.0 [\#118](https://github.com/patrickjahns/ansible-role-promtail/pull/118) ([renovate[bot]](https://github.com/apps/renovate))

## [1.17.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.17.0) (2022-07-08)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.16.0...1.17.0)

**Closed issues:**

- Support pipeline\_stages [\#105](https://github.com/patrickjahns/ansible-role-promtail/issues/105)

**Merged pull requests:**

- chore\(deps\): update dependency grafana/loki to v2.6.0 [\#115](https://github.com/patrickjahns/ansible-role-promtail/pull/115) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency setuptools to v63 [\#114](https://github.com/patrickjahns/ansible-role-promtail/pull/114) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency setuptools to v62.6.0 [\#111](https://github.com/patrickjahns/ansible-role-promtail/pull/111) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency molecule to v4 [\#110](https://github.com/patrickjahns/ansible-role-promtail/pull/110) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update actions/setup-python action to v4 [\#109](https://github.com/patrickjahns/ansible-role-promtail/pull/109) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update robertdebock/galaxy-action action to v1.2.1 [\#107](https://github.com/patrickjahns/ansible-role-promtail/pull/107) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency setuptools to v62.5.0 [\#106](https://github.com/patrickjahns/ansible-role-promtail/pull/106) ([renovate[bot]](https://github.com/apps/renovate))

## [1.16.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.16.0) (2022-04-11)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.15.0...1.16.0)

**Implemented enhancements:**

- Add upstream sync script [\#4](https://github.com/patrickjahns/ansible-role-promtail/issues/4)
- chore\(deps\): update dependency grafana/loki to v2.5.0 [\#103](https://github.com/patrickjahns/ansible-role-promtail/pull/103) ([renovate[bot]](https://github.com/apps/renovate))

**Merged pull requests:**

- chore\(deps\): update dependency setuptools to v62 [\#102](https://github.com/patrickjahns/ansible-role-promtail/pull/102) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update robertdebock/galaxy-action action to v1.2.0 [\#100](https://github.com/patrickjahns/ansible-role-promtail/pull/100) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency setuptools to v61 [\#99](https://github.com/patrickjahns/ansible-role-promtail/pull/99) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update actions/checkout action to v3 [\#98](https://github.com/patrickjahns/ansible-role-promtail/pull/98) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update actions/setup-python action to v3 [\#97](https://github.com/patrickjahns/ansible-role-promtail/pull/97) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency molecule to v3.6.1 [\#95](https://github.com/patrickjahns/ansible-role-promtail/pull/95) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency setuptools to v60.9.2 [\#94](https://github.com/patrickjahns/ansible-role-promtail/pull/94) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency molecule to v3.6.0 [\#93](https://github.com/patrickjahns/ansible-role-promtail/pull/93) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency setuptools to v60.8.1 [\#92](https://github.com/patrickjahns/ansible-role-promtail/pull/92) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency setuptools to v60.6.0 [\#91](https://github.com/patrickjahns/ansible-role-promtail/pull/91) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency setuptools to v60 [\#88](https://github.com/patrickjahns/ansible-role-promtail/pull/88) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency setuptools to v58.5.3 [\#87](https://github.com/patrickjahns/ansible-role-promtail/pull/87) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update robertdebock/galaxy-action action to v1.1.1 [\#83](https://github.com/patrickjahns/ansible-role-promtail/pull/83) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): pin dependencies [\#82](https://github.com/patrickjahns/ansible-role-promtail/pull/82) ([renovate[bot]](https://github.com/apps/renovate))
- chore: add renovate config [\#80](https://github.com/patrickjahns/ansible-role-promtail/pull/80) ([MindTooth](https://github.com/MindTooth))

## [1.15.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.15.0) (2022-01-13)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.14.0...1.15.0)

**Implemented enhancements:**

- Add promtail\_systemd\_service variable \(needed to configure multiple promtail instances\). [\#73](https://github.com/patrickjahns/ansible-role-promtail/pull/73) ([aberes](https://github.com/aberes))

**Merged pull requests:**

- Remove deprecated `include` [\#78](https://github.com/patrickjahns/ansible-role-promtail/pull/78) ([Lithimlin](https://github.com/Lithimlin))
- chore: update to promtail 2.4.2 [\#77](https://github.com/patrickjahns/ansible-role-promtail/pull/77) ([patrickjahns](https://github.com/patrickjahns))

## [1.14.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.14.0) (2021-12-28)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.13.1...1.14.0)

**Implemented enhancements:**

- Allow for custom checksum [\#72](https://github.com/patrickjahns/ansible-role-promtail/pull/72) ([Cyb3r-Jak3](https://github.com/Cyb3r-Jak3))

**Closed issues:**

- Ability to disable checksum check [\#71](https://github.com/patrickjahns/ansible-role-promtail/issues/71)


## [1.13.1](https://github.com/patrickjahns/ansible-role-promtail/tree/1.13.1) (2021-11-28)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.13.0...1.13.1)

**Closed issues:**

- Cannot pull latest version [\#65](https://github.com/patrickjahns/ansible-role-promtail/issues/65)

**Merged pull requests:**

- \[RELEASE\] 1.13.1 [\#69](https://github.com/patrickjahns/ansible-role-promtail/pull/69) ([github-actions[bot]](https://github.com/apps/github-actions))
- Update meta and CI to show Debian Bullseye support. [\#68](https://github.com/patrickjahns/ansible-role-promtail/pull/68) ([twoequaldots](https://github.com/twoequaldots))

## [1.13.1](https://github.com/patrickjahns/ansible-role-promtail/tree/1.13.1) (2021-11-28)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.13.0...1.13.1)

**Closed issues:**

- Cannot pull latest version [\#65](https://github.com/patrickjahns/ansible-role-promtail/issues/65)

**Merged pull requests:**

- Update meta and CI to show Debian Bullseye support. [\#68](https://github.com/patrickjahns/ansible-role-promtail/pull/68) ([twoequaldots](https://github.com/twoequaldots))

## [1.13.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.13.0) (2021-11-10)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.12.0...1.13.0)

**Merged pull requests:**

- chore: bump promtail to 2.4.1 [\#66](https://github.com/patrickjahns/ansible-role-promtail/pull/66) ([patrickjahns](https://github.com/patrickjahns))

## [1.12.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.12.0) (2021-09-10)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.11.0...1.12.0)

**Closed issues:**

- Remove update\_cache or make it optional [\#63](https://github.com/patrickjahns/ansible-role-promtail/issues/63)
- Remove `run\_once: True` in preflight [\#59](https://github.com/patrickjahns/ansible-role-promtail/issues/59)

**Merged pull requests:**

- Add possibility to opt out of APT cache updates [\#64](https://github.com/patrickjahns/ansible-role-promtail/pull/64) ([mweinelt](https://github.com/mweinelt))
- chore: bump promtail to version 2.3.0 [\#60](https://github.com/patrickjahns/ansible-role-promtail/pull/60) ([patrickjahns](https://github.com/patrickjahns))

## [1.11.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.11.0) (2021-04-06)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.10.0...1.11.0)

**Implemented enhancements:**

- chore: bump promtail version to 2.2.1 [\#56](https://github.com/patrickjahns/ansible-role-promtail/pull/56) ([patrickjahns](https://github.com/patrickjahns))

**Closed issues:**

- Version 1.10.0 not available on Galaxy [\#53](https://github.com/patrickjahns/ansible-role-promtail/issues/53)

## [1.10.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.10.0) (2021-04-02)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.9.1...1.10.0)

**Implemented enhancements:**

- chore: bump promtail to 2.2.0 [\#51](https://github.com/patrickjahns/ansible-role-promtail/pull/51) ([patrickjahns](https://github.com/patrickjahns))

**Fixed bugs:**

- ci: ensure the release version is properly parsed in the release pipeline [\#54](https://github.com/patrickjahns/ansible-role-promtail/pull/54) ([patrickjahns](https://github.com/patrickjahns))

**Merged pull requests:**

- \[RELEASE\] 1.10.0 [\#52](https://github.com/patrickjahns/ansible-role-promtail/pull/52) ([github-actions[bot]](https://github.com/apps/github-actions))

## [1.10.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.10.0) (2021-03-11)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.9.1...1.10.0)

**Implemented enhancements:**

- chore: bump promtail to 2.2.0 [\#51](https://github.com/patrickjahns/ansible-role-promtail/pull/51) ([patrickjahns](https://github.com/patrickjahns))

## [1.9.1](https://github.com/patrickjahns/ansible-role-promtail/tree/1.9.1) (2020-12-30)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.9.0...1.9.1)

**Closed issues:**

- Entry\_parser setting is no longer needed in playbook examples [\#47](https://github.com/patrickjahns/ansible-role-promtail/issues/47)

**Merged pull requests:**

- doc: correct links to upstream configuration [\#50](https://github.com/patrickjahns/ansible-role-promtail/pull/50) ([patrickjahns](https://github.com/patrickjahns))
- Remove entry parser setting from example config [\#48](https://github.com/patrickjahns/ansible-role-promtail/pull/48) ([tideline3d](https://github.com/tideline3d))

## [1.9.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.9.0) (2020-12-26)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.8.0...1.9.0)

**Merged pull requests:**

- chore: bump promtail version to 2.1.0 [\#45](https://github.com/patrickjahns/ansible-role-promtail/pull/45) ([patrickjahns](https://github.com/patrickjahns))

## [1.8.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.8.0) (2020-12-25)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.7.0...1.8.0)

**Implemented enhancements:**

- Make role compatible with RHEL linux distributions [\#8](https://github.com/patrickjahns/ansible-role-promtail/issues/8)
- Feature rhel compatability [\#43](https://github.com/patrickjahns/ansible-role-promtail/pull/43) ([patrickjahns](https://github.com/patrickjahns))

**Fixed bugs:**

- Why is the promtail\_config\_positions empty by default? [\#37](https://github.com/patrickjahns/ansible-role-promtail/issues/37)

**Closed issues:**

- Move ansible tests to github actions [\#34](https://github.com/patrickjahns/ansible-role-promtail/issues/34)

**Merged pull requests:**

- CI: fix testing by pinning dependencies [\#44](https://github.com/patrickjahns/ansible-role-promtail/pull/44) ([patrickjahns](https://github.com/patrickjahns))
- doc: improve readme [\#42](https://github.com/patrickjahns/ansible-role-promtail/pull/42) ([patrickjahns](https://github.com/patrickjahns))
- CI: notify galay on a new release [\#41](https://github.com/patrickjahns/ansible-role-promtail/pull/41) ([patrickjahns](https://github.com/patrickjahns))
- Fixes / extends configuration of the positions file [\#39](https://github.com/patrickjahns/ansible-role-promtail/pull/39) ([funkyfuture](https://github.com/funkyfuture))
- ci: move to github actions [\#38](https://github.com/patrickjahns/ansible-role-promtail/pull/38) ([patrickjahns](https://github.com/patrickjahns))

## [1.7.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.7.0) (2020-10-28)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.6.1...1.7.0)

**Implemented enhancements:**

- Chore\(binary\) update promtail to 2.0.0 [\#32](https://github.com/patrickjahns/ansible-role-promtail/pull/32) ([abmurksi](https://github.com/abmurksi))

**Merged pull requests:**

- ci: test with ansible 2.10 [\#36](https://github.com/patrickjahns/ansible-role-promtail/pull/36) ([patrickjahns](https://github.com/patrickjahns))
- fix: fix tests by including new required molecule-docker dependency [\#33](https://github.com/patrickjahns/ansible-role-promtail/pull/33) ([patrickjahns](https://github.com/patrickjahns))

## [1.6.1](https://github.com/patrickjahns/ansible-role-promtail/tree/1.6.1) (2020-09-11)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.6.0...1.6.1)

**Merged pull requests:**

- chore\(binary\): update promtail to 1.6.1 [\#29](https://github.com/patrickjahns/ansible-role-promtail/pull/29) ([abmurksi](https://github.com/abmurksi))

## [1.6.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.6.0) (2020-09-03)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.5.0...1.6.0)

**Fixed bugs:**

- fix: specify provide permissions for file related tasks [\#27](https://github.com/patrickjahns/ansible-role-promtail/pull/27) ([patrickjahns](https://github.com/patrickjahns))

**Merged pull requests:**

- chore\(binary\): update promtail to version 1.6.0 [\#26](https://github.com/patrickjahns/ansible-role-promtail/pull/26) ([secustor](https://github.com/secustor))

## [1.5.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.5.0) (2020-07-29)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.4.0...1.5.0)

**Implemented enhancements:**

- Make role compatible with arm architecture [\#20](https://github.com/patrickjahns/ansible-role-promtail/issues/20)

**Fixed bugs:**

- Replace the rest of the hardcoded references to amd64 with {{ go\_arch }} [\#23](https://github.com/patrickjahns/ansible-role-promtail/pull/23) ([mkeesey](https://github.com/mkeesey))

## [1.4.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.4.0) (2020-05-27)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.3.1...1.4.0)

**Implemented enhancements:**

- feat: add support for arm architecture [\#22](https://github.com/patrickjahns/ansible-role-promtail/pull/22) ([patrickjahns](https://github.com/patrickjahns))
- Promtail 1.5.0 [\#17](https://github.com/patrickjahns/ansible-role-promtail/pull/17) ([patrickjahns](https://github.com/patrickjahns))

## [1.3.1](https://github.com/patrickjahns/ansible-role-promtail/tree/1.3.1) (2020-05-26)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.3.0...1.3.1)

**Fixed bugs:**

- fix: raise privileges of restart handler [\#15](https://github.com/patrickjahns/ansible-role-promtail/pull/15) ([terorie](https://github.com/terorie))

## [1.3.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.3.0) (2020-05-10)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.2.0...1.3.0)

**Implemented enhancements:**

- Include canary [\#1](https://github.com/patrickjahns/ansible-role-promtail/issues/1)
- add support for ubuntu disco [\#13](https://github.com/patrickjahns/ansible-role-promtail/pull/13) ([patrickjahns](https://github.com/patrickjahns))
- Feat add file sd config [\#12](https://github.com/patrickjahns/ansible-role-promtail/pull/12) ([patrickjahns](https://github.com/patrickjahns))

## [1.2.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.2.0) (2020-04-11)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.1.0...1.2.0)

**Fixed bugs:**

- fix: renamed promtail\_config\_scrap\_configs to promtail\_config\_scrape\_configs [\#10](https://github.com/patrickjahns/ansible-role-promtail/pull/10) ([patrickjahns](https://github.com/patrickjahns))

**Merged pull requests:**

- feat: install promtail 1.4.1 by default [\#9](https://github.com/patrickjahns/ansible-role-promtail/pull/9) ([patrickjahns](https://github.com/patrickjahns))

## [1.1.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.1.0) (2020-03-01)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.0.1...1.1.0)

**Implemented enhancements:**

- feat: specify the log level for promtail [\#7](https://github.com/patrickjahns/ansible-role-promtail/pull/7) ([patrickjahns](https://github.com/patrickjahns))

**Merged pull requests:**

- Updated repository settings and added release automation [\#5](https://github.com/patrickjahns/ansible-role-promtail/pull/5) ([patrickjahns](https://github.com/patrickjahns))
- added ansible-later for more indepth static code analysis [\#3](https://github.com/patrickjahns/ansible-role-promtail/pull/3) ([patrickjahns](https://github.com/patrickjahns))

## [1.0.1](https://github.com/patrickjahns/ansible-role-promtail/tree/1.0.1) (2020-02-09)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/1.0.0...1.0.1)

**Fixed bugs:**

- fix: failing installation on ubuntu1604 [\#2](https://github.com/patrickjahns/ansible-role-promtail/pull/2) ([patrickjahns](https://github.com/patrickjahns))

## [1.0.0](https://github.com/patrickjahns/ansible-role-promtail/tree/1.0.0) (2020-02-08)

[Full Changelog](https://github.com/patrickjahns/ansible-role-promtail/compare/87a46bd92a106bffd43e000a4579c1a444bfbf2e...1.0.0)



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
