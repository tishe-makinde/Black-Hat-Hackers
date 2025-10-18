import 'package:flutter/cupertino.dart';
import 'package:trustify_app/core/constants/app_constants.dart';
import 'package:trustify_app/features/verification/presentation/enums/verifier_type.dart';
import 'package:trustify_app/features/verification/presentation/widgets/verifier_controller.dart';
import 'package:trustify_app/features/verification/presentation/widgets/verifier_tab_segment.dart';

class VerifierPage extends StatefulWidget {
  const VerifierPage({super.key});

  @override
  State<VerifierPage> createState() => _VerifierPageState();
}

class _VerifierPageState extends State<VerifierPage> {
  static const EdgeInsets _padding = EdgeInsets.all(8.0);
  VerifierType _selectedVerifier = VerifierType.link;
  @override
  Widget build(BuildContext context) {
    final CupertinoThemeData theme = CupertinoTheme.of(context);
    return CupertinoPageScaffold(
      navigationBar: CupertinoNavigationBar(
        leading: Row(
          children: [
            Image.asset('assets/images/verify_green.png'),
            Text(AppConstants.appName,
                style: theme.textTheme.navLargeTitleTextStyle),
          ],
        ),
      ),
      child: Padding(
        padding: _padding,
        child: SafeArea(
          child: Column(
            children: [
              Center(
                child: CupertinoSlidingSegmentedControl(
                  children: <VerifierType, VerifierTabSegment>{
                    VerifierType.link: VerifierTabSegment(
                      icon: CupertinoIcons.link,
                      title: 'Link',
                    ),
                    VerifierType.image: VerifierTabSegment(
                      icon: CupertinoIcons.photo,
                      title: 'Image',
                    ),
                  },
                  groupValue: _selectedVerifier,
                  onValueChanged: (VerifierType? verifier) {
                    if (verifier != null) {
                      setState(() {
                        _selectedVerifier = verifier;
                      });
                    }
                  },
                ),
              ),
              VerifierController(selectedVerifier: _selectedVerifier),
            ],
          ),
        ),
      ),
    );
  }
}
