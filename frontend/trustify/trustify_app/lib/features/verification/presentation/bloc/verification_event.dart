part of 'verification_bloc.dart';

@immutable
sealed class VerificationEvent {}

final class VerificationLink extends VerificationEvent {
  final String url;
  VerificationLink(this.url);
}
